<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://i.ibb.co/njkqjW7/17984.png" alt="Logo" width="280" height="80">
  </a>
<br /><br />
  <h3 align="center">Shopium Faker</h3>

  <p align="center">
    The Following is a general presentaion of our project 
    <br /><br /><br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>

<div>
<br />
<br />
<br />
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<a name="about-the-project"></a>
<!-- ABOUT THE PROJECT -->
## About The Project

* Shopium Faker is a data faker system made for **[Shopium][shopium-url]** to build a similar fake database.


* The fake database generated tables are connected based on **[Shopium][shopium-url]**'s logic data structure.


* The data aregenerated mainly using **[Faker][faker-url]** and other resources to match our requirements


* This project requires a connection url from **[Mongo Atlas][atlas-url]** to insert data in your preferred database/cluster



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="built-with"></a>
### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
<br />
<br />
* [Faker][faker-url]
* [googletrans][React-url]
* [MongoDB][Vue-url]




<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="getting-started"></a>
<!-- GETTING STARTED -->
## Getting Started

Before we proceed , this project was designed to simulate [Shopium][shopium-url]'s Database to better understand and predict our future performance :
<br />

  <summary>Shopium Tables Structure</summary>
  <ol>
    <li>
      Users
        <ul>
        <li>_id : ID</li>
        <li>nom : string</li>
        <li>prenom : string</li>
        <li>pays : string</li>
        <li>ville : string</li>
        <li>email : string</li>
        <li>password : string</li>
        <li>role : string("admin", "subscriber")</li>
        <li>photo : string</li>
        <li>cloudinary_id : string</li>
        <li>verified : Boolean(75%True/25%False)</li>
        <li>codeParrainage : Int (five digits)</li>
        <li>amis : IDs</li>
        <li>friendRequest : IDs</li>
        <li>sendRequest : IDs</li>
        <li>createdAt : string (Date/Time)</li>
        <li>updatedAt : string (Date/Time)</li>
        <li>date : string (Date)</li>
        <li>genre : string("H", "F")</li>
      </ul>
    </li>
<br /><br />
    <li>
      Products
        <ul>
        <li>_id : ID</li>
        <li>name : string</li>
        <li>price : int</li>
        <li>photo:         [string] (Photos Urls)</li>
        <li>categoryId:    category IDs</li>
        <li>fabricant:     fabricant ID</li>
        <li>offer:         offers IDs</li>
        <li>logo:          string (URL)</li>
        <li>isLiked:       Boolean(True/False)</li>
        <li>isnew:         Boolean(True/False)</li>
        <li>createdAt:     string (Date/Time)</li>
        <li>updateddAt:    string (Date/Time)</li>
        <li>barcode:       string (EAN13)</li>
      </ul>
    </li>
<br /><br />
    <li>
      Category  
        <ul>
        <li> _id:           ID</li>
        <li> category_id:           ID</li>
        <li>name:          string</li>
        <li>createdAt:     string (Date/Time)</li>
        <li>photo:         [string] (Photos Urls)</li>
        <li>categoryId:    category IDs</li>
        <li>updatedAt:     string (Date/Time)</li>
      </ul>
    </li>
<br /><br />
    <li>
      SubCategory  
        <ul>
        <li> _id:           ID</li>
        <li> sub_id:           ID</li>
        <li> category_id:           ID</li>
        <li>createdAt:     string (Date/Time)</li>
        <li>updatedAt:     string (Date/Time)</li>
      </ul>
    </li>
<br /><br />
    <li>
      Fabricant  
        <ul>
        <li>_id:           ID</li>
        <li>fab_id:           ID</li>
        <li>name:          string</li>
        <li>password:      string</li>
        <li>logo:          string</li>
        <li>phone:         string</li>
        <li>createdAt:     string (Date/Time)</li>
        <li>updateddAt:    string (Date/Time)</li>
      </ul>
    </li>
<br /><br />
    <li>
      Offers  
        <ul>
        <li>_id:           ID</li>
        <li>offer_id:           ID</li>
        <li>startDate:           ID</li>
        <li>expirationDate:           ID</li>
        <li>condition:          string</li>
        <li>description:      string</li>
        <li>quantity:          string</li>
        <li>percentage:         string</li>
        <li>product_id:         Int</li>
        <li>createdAt:     string (Date/Time)</li>
        <li>updatedAt:     string (Date/Time)</li>
        <li>isNew:          Boolean</li>
        <li>views:         Int</li>
        <li>avgReviews:         Int</li>
        <li>productName:         string</li>
      </ul>
    </li>
<br /><br />
    <li>
      Reviews  
        <ul>
        <li>_id:           ID</li>
        <li>rev_id:           ID</li>
        <li>offer_id:           ID</li>
        <li>user_id:           ID</li>
        <li>username:          string</li>
        <li>text:      string</li>
        <li>image:          string</li>
        <li>phone:         string</li>
        <li>rating:         Int</li>
      </ul>
    </li>
<br /><br />
    <li>
      Fidelite  
        <ul>
        <li>fid_id:           ID</li>
        <li>user_id:        ID</li>
        <li>data:          string (Barcode EAN13)</li>
        <li>format:        string</li>
      </ul>
    </li>
<br /><br />
    <li>
      Ribs  
        <ul>
        <li>rib_id:           ID</li>
        <li>user_id:        ID</li>
        <li>numero:        string</li>
        <li>type:          string</li>
        <li>banque:        string</li>
        <li>createdAt:     string (Date/Time)</li>
        <li>updateddAt:    string (Date/Time)</li>
      </ul>
    </li>
  </ol>

<br /><br />
### Prerequisites

This is a list of different main modules to install before implementing our project
* Python
  ```sh
  npm install npm@latest -g
  ```
* pip
  ```sh
  npm install npm@latest -g
  ```
* Tesseract
  ```sh
  npm install npm@latest -g
  ```
<br /><br />
### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/firas122/ShopiumFake
   ```

2. Install **pip** packages
   ```sh
   pip install -r requirements.txt
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
* Run the faker using the command above and stay on the terminal to go through the inputs procedure to specify the number of objects to generate in each table(some tables number are fixed you'll be informed by the terminal on why and how to extend those kind of tables):
<br /><br />
```sh
   python /project_directory_path/main.py
```
<br /><br />
* Terminal output will be as a guide through the inputs process as illustrated above :

<br /><br />






## Roadmap

- [x] Generate Fake Data
- [x] Data customized Generation
- [x] Assure relation between generated tables
- [ ] Multi-Ticket Forms support
- [ ] Design a Machine learning approach


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Shopium - [@Shopium](https://twitter.com/your_username) - shopium.local@gmail.com

Project Link: [https://github.com/firas122/Scan](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[shopium-url]: https://www.shopium.tn/
[atlas-url]: https://www.mongodb.com/atlas/database
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[faker-url]: https://fakerjs.dev/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://pypi.org/project/googletrans/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 