RRad was a piece of software I programmed as part of a computer graphics course at university, and was the direct lead-up to my Maser's Thesis, the more sophisticated [RTRad](https://benjamin.kahl.fi/build/projects/rtrad/detailed.html).

It is a GPU-based implementation of the Radiosity algorithm made with the open-source API OpenGL and it highlights with clarity how visibility is the only major hurdle that prevents the widespread adoption of GPU-based radiosity.

RRad approximates a scene through basic geometric shapes (spheres and triangles) and then loops over each shape and performs a simple, discrete ray-intersection
on each. This geometric approximation is hard-coded into the shader’s code itself, making the application simple and lightweight, but entirely unsuitable to complex
environments. Fig. 4.2 shows the default RRad scene with a lightmap of 512 × 512 pixels (~260k elements), for which a single bounce of light requires approx. 1.5 seconds of computation time on a GeForce RTX 2070S GPU.

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ZGagw0xYKAM?si=vNfPEIRMAH8TUy06" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>