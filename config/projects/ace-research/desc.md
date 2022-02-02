As a team of 5 we built a customized research library which has been in use under https://animalcharityevaluators.org/researchlibrary/ since 2016. The complete source code can be found under https://github.com/FUB-HCC/ACE-Research-Library.
The goal of the ACE Research Library project was to provide ACE with an interface that aids the staff in entering new articles and papers and to provide the visitors of ACE’s website with powerful search and drilldown mechanisms. The software is open source and agnostic of the user so that it may be used by anyone with similar requirements on their data organization.

## Motivation

Donations to animal charities are usually not allocated in correspondence of their need. In accordance to the principles of [effective altruism](https://en.wikipedia.org/wiki/Effective_altruism), the possible good done by animal welfare donations should be enhanced by shifting respective donations to be more effective, which is best done by raising awareness and keeping the public informed through organized research papers and evidence.

Academic research into animal welfare, especially high-quality, quantitative research, is still relatively scarce, but research from areas as diverse as economics, sociology, psychology, marketing, medicine, history, political science, and even computer science can at times inform policy and priorities setting to advance animal welfare.

<img src="config/projects/ace-research/graph.jpg" alt="graph" style="width:50%">

The nonprofit organization Animal Charity Evaluators (ACE) is optimistic that the coming years will see an increase in high-quality targeted research into animal welfare, so now more than ever there is value in collecting, pruning, and organizing the research such that other researchers and implementing parties – companies, foundations, nonprofits, and government offices among them – can quickly gain an overview of it.

Just such a repository of annotated research was being maintained by the organization and was publicly accessible on its website. But since it was but a list of links and abstracts organized into twelve broad categories, which was rapidly reaching its limits as the volume of research increased, we proposed a complete rework of their system.


## Digital Library

According to Jeng (2005), "[a] digital library is an information system over a network that is organized and well-managed, and that supports the creation, use, and searching of digital objects. [A] digital library should be looked as a tool that supports user's information task. Users are looking for an information system that is easy and intuitive to use."

Together we looked at and analyzed a number of existing research-libraries to discern what features would be of the essence. In combination with some user tests we made the primary observations that our features required at least:

- Full text search with auto-complete
- Different categories
- Time-interval filters
- Automatic keyword extraction
- Metadata suggestions


## Project Team

### Members

Our team consisted of:

Name                 | Degree Course                 | Roles
-------------------- | ---------------------------------- | ------------
Dominik Bechinie     | Master of math and CS         | Flexible
Denis Drescher       | Master of CS                  | Software architect, customer contact
Maximilian Göhner    | Master of biology and CS      | Team manager
Benjamin Kahl        | Bachelor of CS                | Backend Development
Taras Kolba          | Bachelor of CS                | Frontend Development

Additionally we were supervised by [Prof. Müller-Birn](https://www.mi.fu-berlin.de/en/inf/groups/hcc/members/professor/mueller-birn.html) at the human-centered computing group of the [FU-Berlin](https://www.fu-berlin.de/en/).

![picture of the team](config/projects/ace-research/splash.jpg)

## Advanced Technologies

Broadly, the project builds on top of **Django** web framework with a wordpress front-end.

To provide all the tools that would enable us to maintain a modular **MVC architecture**, the separation of concerns that comes with the orthogonality of the modules were essential for us to work independently and minimize our communication overhead. The programmable API was be **RESTful** and built upon the **JSON standard**, which is light in syntax and easy to use from a JavaScript frontend.

The **Gunicorn** webserver works well with Django and provides high performance. While we use an **Nginx** server as reverse proxy in front of Gunicorn for static file serving and possibly caching, Gunicorn does the heavy lifting of serving the dynamic content. **PostgreSQL** serves as our primary storage. **Whoosh** is our chosen search engine.

For organization we utilized **Trello** as a Kanban board and **Slack** for communication. We utilized several slack-bots that integrated out workflow tightly with github and trello.

![picture of backend](config/projects/ace-research/backend.jpg)

## Backend Structure

Over the course of the projects development the underlying database model changed on multiple occasions. We ultimately opted for the model depicted below:

![picture of database](config/projects/ace-research/databasemodel.jpg)

The interfaces between front- and back-end were defined at three distinct endpoints.

- The list endpoint for querying certain pages on a complete list of all resources.
- The suggest endpoint for the autocomplete function.
- And, most importantly, the search endpoint.

Their precise specification is depicted below.

![picture of endpoints](config/projects/ace-research/Endpoints.png)

## Quality Control

Once the project was nearing completion we conducted several user-tests and interviews with a variety of test subjects.

Whilst the interviews helped us to outline the desired requirements, user-tests were a powerful form of quality control of our actual product.
In these, test subjects were given either administrative or end-user related tasks and recorded whilst (attempting) to perform these. The recordings of these can be found [here.](https://www.youtube.com/watch?v=UZcDUCeMcpU&list=PLQu2cPkjtBZiIohj9bTwi721vAKbKdf_0&index=1&ab_channel=MaximilianG%C3%B6hner)

![picture of endpoints](config/projects/ace-research/QC.jpg)

## Git Statistics

This video generated with [Gource](https://gource.io/) illustrates our development process in highly entertaining (yet also confusing) manner:

[Youtube Link](https://www.youtube.com/watch?v=UXepjw-Eudw)

Alternatively, this graph displays a rough timeline of github-commits in relation to their respective categories:

![picture of git stats](config/projects/ace-research/git-stats.jpg)

## The Product

Ultimately our team received high praise from both our supervisor as well as ACE themselves. The completed research library has been in use under [animalcharityevaluators.org/researchlibrary](https://animalcharityevaluators.org/researchlibrary/#/) since 2016 and continues to be frequently updated and maintained.

![picture of library site](config/projects/ace-research/product.jpg)
