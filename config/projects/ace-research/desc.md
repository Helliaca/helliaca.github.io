Donations to animal charities are usually not allocated in correspondence of their need. In accordance to the principles of [effective altruism](https://en.wikipedia.org/wiki/Effective_altruism), the possible good done by animal welfare donations should be enhanced by shifting respective donations to be more effective, which is best done by raising awareness and keeping the public informed through organized research papers and evidence.

Academic research into animal welfare, especially high-quality, quantitative research, is still relatively scarce, but research from areas as diverse as economics, sociology, psychology, marketing, medicine, history, political science, and even computer science can at times inform policy and priorities setting to advance animal welfare.

<img src="config/projects/ace-research/graph.jpg" alt="graph" style="width:50%">

The nonprofit organization Animal Charity Evaluators (ACE) is optimistic that the coming years will see an increase in high-quality targeted research into animal welfare, so now more than ever there is value in collecting, pruning, and organizing the research such that other researchers and implementing parties – companies, foundations, nonprofits, and government offices among them – can quickly gain an overview of it.

Just such a repository of annotated research was being maintained by the organization and was publicly accessible on its website. But since it was but a list of links and abstracts organized into twelve broad categories, which was rapidly reaching its limits as the volume of research increased, we proposed a complete rework of their system.

As a team of 5 we built a customized research library which has been in use under https://animalcharityevaluators.org/researchlibrary/ since 2016. The complete source code can be found under https://github.com/FUB-HCC/ACE-Research-Library.
The goal of the ACE Research Library project was to provide ACE with an interface that aids the staff in entering new articles and papers and to provide the visitors of ACE’s website with powerful search and drilldown mechanisms. The software is open source and agnostic of the user so that it may be used by anyone with similar requirements on their data organization.


## Project Scope

In detail, we set out to provide:

- a user-friendly interface for the staff for entering research papers into a database that suggests meta data to the staff member based on some that was already entered,
- optionally, Neonion as an alternative input method,
- a programmable API, so the database is agnostic to the frontend that queries it,
- a sample frontend that allows access to the database from a website,
- a full-text search that can efficiently find words and phrases via an index of the linguistically analyzed body text of the research papers, and
- an automatic keyword or topic extraction that provides a more fine-grained alternative to the current categorization and, in ideal cases, automates the keyword annotation.


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
