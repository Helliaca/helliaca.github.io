A convex partition of a pointset consists of a planar subdivision of its convex hull so that all faces are empty and convex. Finding a partition with the minimum amount of edges (or faces), is still a problem of unknown complexity.

The [CG:SHOP 2020 competition](https://cgshop.ibr.cs.tu-bs.de/competition/cg-shop-2020/#problem-description) put forth a large number of pointsets alongside the challenge to compute their convex partitions that incorporate the least amount of edges.

With a team of four members we set out to give it our best shot using rudimentary, symbolic algorithms. The [github repository](https://github.com/SemjonKerner/convex_polygons) of our project includes all of our computed results as well as their respective algorithms.

If you deem the explanation on this site insufficient or simply want to know more about our employed algorithms, I highly suggest to check out our written report on our proceedings which you can find [here](https://github.com/SemjonKerner/convex_polygons/blob/master/texinput/report.pdf) as well as the slides of our final presentation, which can be found [here](https://github.com/SemjonKerner/convex_polygons/blob/b5412ddf3189458d07803e934d98bb67e8e7cc36/texinput/convex_polygons.pdf).

The problem, as stated by the competition is:  
_Given a set S of n points in the plane. The objective is to compute a plane graph with vertex set S (with each point in S having positive degree) that partitions the convex hull of S into the smallest possible number of convex faces. Note that collinear points are allowed on face boundaries, so all internal angles of a face are at most pi_

<img alt="example of a convex partition" src="config/projects/convex_polygons/banner.png">

# Proceedings

## Preparations

The field of algorithmic geometry poses problems that, due to their complexity, can get out of hand quickly without a robust data-structure to support them. Since we were planning on implementing several algorithms, we opted for the stalwart [DCEL](https://en.wikipedia.org/wiki/Doubly_connected_edge_list), or 'doubly connected edge list'.

This data-structure handles polygonal data in the form of doubly connected edges. Each edge has a twin (essentially its inverse) as well as a predecessor `prev` and successor `next`. At any given vertex the connected edges can be traversed in counter-clockwise order by iterating through each twin and successor.[^1]

![image of a dcel](config/projects/convex_polygons/dcel.png)

[^1]: For more information refer to our [project pdf](https://raw.githubusercontent.com/SemjonKerner/convex_polygons/master/texinput/report.pdf)

There are a manifold of libraries in all programming languages that offer any common DCEL functionality. However, as some of the pointsets provided by the competition reached into *millions* of points, performance would be of the essence. To keep a good overview of all our computational operations, we decided to implement a DCEL variant ourselves. Although some additional effort, this allowed us to create a highly minimalized variant that only performs the actions we require it with good performance. Our DCEL implementation can be found under in one of our project in [HDCEL.py](https://github.com/SemjonKerner/convex_polygons/blob/master/bin/HDCEL.py).

## Benchmark algorithms

For fist step we wanted to ensure that we could compute at least one half-way decent result for each pointset provided by the competition, so we decided to start simple.

As one of our first algorithms we implemented the a simple *nested convex hull* (or [convex layers](https://en.wikipedia.org/wiki/Convex_layers)) approach. This one simply computes the outermost convex hull of the pointset, then recursively repeats this step for all remaining points until none are left. As a final step the individual hulls need to be connected in a way as to produce a convex partition.

For our second approach we coined the name *convex waves*. This was a more unique, even novel approach compared to nested hulls, whilst maintaining an even higher degree of performance.
Here, we start at any given (or random) point in the plane and perform a radial sweep-line that incorporates all vertices into the partition in order of their distance to the startpoint.
A new vertex is integrated into the partition by connecting it to all vertices on the hull that are 'visible' to it (two vertices are mutually visible if no edges lie in-between them). Subsequently, the hulls edges are tested for redundancy, then removed or kept respectively.  Additionally, the presence of collinear points on the hull may permit the removal of some of the created edges. Lastly,  the separately maintained convex hull is updated to accommodate the newly annexed vertex.

These two algorithms are both extremely fast and fall within a complexity of O(log n). Thanks to its dependence on a starting-point, *convex waves* can also be executed in parallel multiple times on a single instance. For randomly scattered vertices, this tends to provide better results than nested hulls.

Thanks to their considerable speed we were able to quickly produce a passable solution to each pointset provided in the competition, albeit we did suffer some setbacks when a new batch was released that included sets with a large number of colinear vertices. However, despite these generally positive results, both of our algorithms traded computational expense for a sub-optimal result. The image below illustrates the solution of a convex wave on an instance of 500 vertices:

![image of conv partition](config/projects/convex_polygons/conv_wave_drawbacks.png)

## Advanced algorithms

### Merged convex Waves

In an attempt to break up the inauspicious pattern produced by a single convex wave, we devised a variant consisting of multiple wave-instances running in tandem. Whenever two of these would collide, the instances are merged into one. The intent was to maximize the desirable results single convex waves produced in the vicinity of their starting points whilst curtailing the circular patterns depicted above.

The basic idea of a 'merge' was simple:

- *Calculate visible bounds:* We compute the outermost, mutually visible vertices on each hull.
- *Query for intermediate points:* Using the foregoing visible bounds, we find all vertices that lie in-between both hulls which remain unclaimed by either.
- *Break up occluding hulls:* If any of these vertices are occupied by other wave-instances, we clear these of all their connected edges.
- *Repair broken instances:* If we cleared any vertices in the last step, we recalculate the convex hulls of the instances they belonged to and triangulate ruptures caused by the previous step.
- *Allocate intermediate points:* The points in-between both instances we divide into two domains by a line and correspondingly allocate them to the respective instance.
- *Integrate intermediate points:* In accordance to the foregoing allocation, we integrate each intermediate vertex into their respective hull using the regular convex wave iterative procedure.
- *Connect instances:* By advancing along the mutually visible bounds, we connect both hulls.

However, in practice, the implementation of a fully functional merging algorithm proved to be more challenging than anticipated. Two or more instances can be arranged in a plethora of unusual predicaments that are left unhandled by the above given steps. We implemented a semi-functional variant of these steps by handling all edge cases individually.

After testing, our central findings were that our merged-approach produced on average 10% more edges than the best solutions computed by a single convex wave. In addition, optimization possibilities were scarce, making it not only our worst performing but also our slowest algorithm.

### Pass-based convex waves

In light of the foregoing, we made the decision to avert the complications of a merging step by opting instead for a pass-based variant. Ultimately, this approach proved to be our best one. It erforms a series of sequential procedures where the output of a previous step is used as input for the next one. In order for this pipeline to function correctly, the input and output of each pass must conform to a strict specification, which we accomplished by employing several intermediate passes.

The exact specification of each pass, as well as the steps they perform can be read in our [project pdf](https://raw.githubusercontent.com/SemjonKerner/convex_polygons/master/texinput/report.pdf), but it roughly boils down to this:

- Grow single convex polygons at given startpoints. If the given points are chosen wisely, this should help secure the largest faces/areas of the partition.
- Gather stray points by performing the step above for all remaining unconnected vertices.
- Integrate any produces 'island'-polygons into their surrounding area and enclose the whole system by computing the convex hull.
- Of the partition produced so far, all inflex points are resolved on an individual basis.
- Lastly we perform a stray-point integration pass as well as a cleaning pass.

This algorithm performed best on most instances. It was naturally slower than _Nested Hulls_ and _Single Convex Wave_.

### Start Points
For _Pass Based_ we calculated a set of start points for each instance. We considered multiple approaches, like clustering with kmeans or heatgrids. Eventually we settled with another approach on Delaunay Triangulation. This approach achieved very good start point distributions.

- A Delaunay triangulation is calculated on all instance points. This leaves us with a set I of edges in a triangulation.
- A second Delaunay triangulation is calculated on the midpoints of edges in I. This triangulation yields a set S of edges.
- The edges in S are ordered by the corresponding edges in I, in a way that the edge in S is directed from the midpoint of the longer edge in I to the midpoint of the shorter edge in I.
- For every midpoint the algorithm counts the outgoing edges in I and sorts the resulting list by the degree.

This approach chooses start points between all instance points in order to eliminate longer edges in a _neighborhood_ of edges. That way bigger polygons shall be created first - not in area size, but in number of vertices. Sadly this algorithm didn't show as much of an effect on _Pass Based_ as hoped.

## Results

The following charts portray the number of instances solved by each of the three algorithms in our final submission:

![graph](config/projects/convex_polygons/results_graph.png)

### Strengths and Weaknesses

When confronted with inputs based on isotropically spread points as well as image- or brightness-based, our pass based algorithm proved to be an indispensable benefit to our over-all performance. It vastly outperformed both other algorithms, albeit at a significantly higher computational cost.

![graph](config/projects/convex_polygons/graphs2.jpg)

For artificially assembled instances of mostly collinear points, the nested hulls algorithmproved highly invaluable. To the naked eye, the image below  may initially appear as a victory for passed-based, but this is mostly due to the areas being stretched out more evenly. The nested hulls approach produces longer squares by combining multiple vertices into a single chain.

![graph](config/projects/convex_polygons/graphs3.jpg)

The single convex wave algorithm was the fastest and acted as a useful fallback for the few cases that pass-based was unable to provide a solution for. The growth of computation time can be observed in the following image: (Note: all times were recorded on an AMD Ryzen 1700)

![graph](config/projects/convex_polygons/graphs4.jpg)

The image below shows our solutions to all orthogonal (diamond  shape) and regular instances (plus-shape). As can be observed, the pass based algorithm dominates throughout most of the larger instances. When it comes to instances with many collinear points (at the top) nested hulls and pass based are mostly at an impasse, with nested hulls scoring the majority of solutions.

![graph](config/projects/convex_polygons/graphs5.jpg)

Here is our score over time:

![graph](config/projects/convex_polygons/graphs6.jpg)
