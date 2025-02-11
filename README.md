# The Adventurer's Rest

## Overview

### Purpose
The Adventurer's Rest is an online Dungeons & Dragons character creation and management tool. It provides an intuitive interface for creating a character conforming to the subset of Dungeons and Dragons rules contained within 
the [Systems Reference Document](https://www.dndbeyond.com/resources/1781-systems-reference-document-srd?srsltid=AfmBOooY4RPy4pqzFizxz7M8g6XqFSs6ig6Iiy24rGq_g1TwqeZZatup) - a subset of the core Dungeons and Dragons rules that are released under the Creative Commons licence.
It also provides an online character sheet, displaying the character's details in an easy-to-digest layout.


### Target Audience
The target audience for this website is Dungeons & Dragons players (current or prospective) that are looking for an easy way to manage their Dungeons & Dragons characters. The site gives them a simple way to create, store and share
their characters, as well as to browse other users characters for inspiration.

![responsive-about-screenshot](https://github.com/user-attachments/assets/230dd2b8-641f-4792-aca3-4ce81b8e0e07)


[Link to deployed site](https://dnd-character-creator-196a1c69fe18.herokuapp.com/)

## UX Design Process

The project board including user stories can be found [here](https://github.com/users/Adam-Campbell/projects/3).

The two most complex views on this website are the Character Editor and Character Detail views, and both of these views required a significant amount of data to be displayed in a clear manner that was easy to interact with. I therefore made the decision to forgo wireframes and to instead just design it directly in the browser where I could interact with it in the manner that a user would, and could also see how it looked with varying amounts of content. I experimented with different layout configurations and UI components to create the layouts, and was able to iterate efficiently thanks to Bootstrap. I made use of UX patterns such as accordions to hide certain details from the user until they were ready to look for them, in order to avoid overwhelming the user with information.

**Character list view**  
![responsive-character-list-screenshot](https://github.com/user-attachments/assets/bc68a95a-564d-41a7-aa95-2af6cbe05345)

**Character detail view**  
![responsive-character-detail-screenshot](https://github.com/user-attachments/assets/6c99020f-d077-4f8b-a82c-8364f1efb666)

**Character editor mobile view**  
![responsive-editor-mobile-screenshot](https://github.com/user-attachments/assets/ee25b4be-e6fd-418e-baa6-ecf17757725b)

**Character editor tablet view**  
![responsive-editor-tablet-screenshot](https://github.com/user-attachments/assets/536f2162-6439-4616-b4b1-ee60ae42e950)

**Character editor desktop view**  
![responsive-editor-desktop-screenshot](https://github.com/user-attachments/assets/32e053c0-bedd-4c13-bc3e-11da9d3bc95a)

I utilised the following colour scheme throughout the site:

![color-palette-screenshot](https://github.com/user-attachments/assets/14bf9b6a-cd1c-49a9-8e56-581d0cc81192)

I sourced the fonts from Google Fonts - I used Cinzel for the headings and Cabin for the body text.

![google-fonts-screenshot](https://github.com/user-attachments/assets/b73e4ab9-2d44-4a03-a8f8-3a2cb86a5e0f)

### Accessibility Considerations
I ensured that colour contrasts were sufficient throughout the site, and that fonts were of sufficient size. Semantic HTML has been used where appropriate, and all form controls are properly labelled. 



## Key Features

- **Authentication:** Authentication was handled by django-allauth, and I made some adjustments to the default HTML templates it uses.
- **Character creation and editing:** The character editor allows the user to create a character adhering to the rules given in the Dungeons and Dragons Systems Reference Document (SRD). The editor reacts according to the choices that the user has made, adjusting the options it presents to ensure that the created characters adhere to the SRD. The editor was built with [AlpineJS](https://alpinejs.dev/) which handles all of the reactivity, and it communicates with the backend via the Fetch API.
- **Character sheets (Character Detail):** The character detail view essentially functions as an online character sheet for a character that a user has created. It takes all of the character information and displays it in an easy-to-digest manner, using responsive design principles to ensure that it looks good at all screen sizes.
- **Character browsing:** Users can browse all publicly available characters, filtering by race and class.
- **Public and private characters:** Users can choose at any time whether they want one of their characters to be public or private. Any private characters can only be viewed by the user that created it.
- **Character 'likes':** Users can 'like' a character, increasing its publicly displayed 'like' count, and also saving it to the users profile under the Liked Characters section.
- **Character cloning:** Users can clone a publicly viewable character, which creates a copy of it in the character editor for them, which they can then use as the starting point for one of their own characters.
- **Image uploading:** Users can upload an image both for their character, and for themselves on their user profile. Uploaded images are cropped to a square (1:1) aspect ratio, and this is handled on the front end by [CropperJS](https://fengyuanchen.github.io/cropperjs/).
- **Character image generation:** The users can choose to generate an image based on their character. This is achieved by taking the characters appearance data from the character editor and using the OpenAI API to feed the data into Dall-E, which then creates the image.




## AI Implementation and Orchestration

- **Code creation:** I utilised Copilot to assist with code creation at various points. It was useful when dealing with parts of Django that I wasn't yet familiar with, and was especially useful for getting me up to speed with libraries I hadn't used before such as [CropperJS](https://fengyuanchen.github.io/cropperjs/).
- **Debugging:** Copilot also proved useful for debugging, although somewhat inconsistently. Sometimes it was very helpful, other times it didn't do much good and I probably would have been better off debugging the issue by myself.
- **Asset generation:** I used Dall-E to generate artwork for the site, including the illustrated images on the about page and some placeholder images. It was quite effective at generating the illustrated artwork, but less so for the placeholders - it took a bit of effort to get it to stop putting extra details into the image.
- **Dynamically creating character images:** In order to dynamically generate character images for the user, I utilised the OpenAI API, which I interacted with through the official openai Python package. At first I attempted to take the appearance data from the character editor and feed it straight into Dall-E as key:value pairs, but this led to very poor and inconsistent results. In the end, I decided to first feed the key:value pairs into the gpt-4o-mini model so that it could generate a natural language description of the character, which I then took and combined with some artwork style instructions and fed it into Dall-E. This produces reasonable results, but they are still somewhat inconsistent. I suspect that it isn't possible to get a high-level of consistency with this approach.





## Testing and Validation

All features were manually tested, both for the Python backend code and the JavaScript frontend code. Bugs were discovered at several points during development, but were quickly dealt with.  
All JavaScript code was ran through JSHint, all Python code was validated with a PEP 8 validator. All HTML and CSS was ran through validators. All issues identified during this process were dealt with, and then the files we revalidated. 
All pages of the deployed site were run through lighthouse.

The screenshots are included below.
![main_views-screenshot](https://github.com/user-attachments/assets/1bbe70a1-fd6e-4062-8ff4-d4401452d296)
![main_urls-screenshot](https://github.com/user-attachments/assets/a576da72-2114-463d-8f38-f25cc00247f3)
![userprofile_views-screenshot](https://github.com/user-attachments/assets/438703d0-9b71-454a-bb18-39d535e2a895)
![userprofile_urls-screenshot](https://github.com/user-attachments/assets/3a65f96a-353f-4094-911c-6b57dd4ea671)
![userprofile_signals-screenshot](https://github.com/user-attachments/assets/66c529b9-c492-4b8c-96b8-d2cb0196dd31)
![userprofile_models-screenshot](https://github.com/user-attachments/assets/c9f2f357-c661-41b5-a085-4efe6a0fd498)
![userprofile_forms-screenshot](https://github.com/user-attachments/assets/e789b7f2-80ae-4307-9d48-91d1b55261f6)
![userprofile_apps-screenshot](https://github.com/user-attachments/assets/f64c5ca5-3579-43cc-9960-646d847b8a71)
![userprofile_admin-screenshot](https://github.com/user-attachments/assets/bb221675-5160-46d7-a6f4-d5dcfa877218)
![characters_views-screenshot](https://github.com/user-attachments/assets/c6300971-7bb5-43eb-a9b9-f3b52c372e54)
![characters_urls-screenshot](https://github.com/user-attachments/assets/2090e7b0-10a0-400c-8c2e-02e4b0f45cf3)
![characters_models-screenshot](https://github.com/user-attachments/assets/bc084b33-be9d-43fa-abb5-09f18897f5eb)
![characters_forms-screenshot](https://github.com/user-attachments/assets/38c8bc25-bf56-4283-ad5b-7c8906261fd5)
![characters_data_utils-screenshot](https://github.com/user-attachments/assets/81ca28a3-f722-4edf-a9d9-b79ba1c05cd0)
![characters_create_characters-screenshot](https://github.com/user-attachments/assets/93e9f1ec-535b-44ba-b0dd-b073b84b2f82)
![characters_admin-screenshot](https://github.com/user-attachments/assets/7c479b26-d338-4874-a1ce-5259da35e3b7)
![character-editor-js-screenshot](https://github.com/user-attachments/assets/4a297e97-650e-4d9d-b9ae-ee52b27f49e9)
![character-detail-js-screenshot](https://github.com/user-attachments/assets/2c726737-d346-4108-bd62-337bd8d283e0)
![utils-js-screenshot](https://github.com/user-attachments/assets/d2604731-ec94-4fc8-9d8a-41323e823862)
![user-profile-js-screenshot](https://github.com/user-attachments/assets/43966d67-c10d-4956-8fb6-7f4b6361b0eb)
![toast-js-screenshot](https://github.com/user-attachments/assets/4b263dfe-07ef-418d-8794-932f51e4fcaf)
![character-editor-html-screenshot](https://github.com/user-attachments/assets/7d882c0e-3ad2-4c50-9f99-eea9b83cdc75)
![character-detail-html-screenshot](https://github.com/user-attachments/assets/7a077180-e3e8-48b2-8966-8898ae8f7443)
![about-html-screenshot](https://github.com/user-attachments/assets/19f98e1c-9c5d-4dc3-8a0d-77a22bb91b27)
![user-profile-html-screenshot](https://github.com/user-attachments/assets/7914ad55-f006-4cdf-b575-23d30af57563)
![characters-list-html-screenshot](https://github.com/user-attachments/assets/c1ca4859-f1b9-4b09-903c-ee0177b7cbec)
![css-screenshot](https://github.com/user-attachments/assets/1e4ea5f7-6598-4462-bb27-2c37bc8410c8)
![userprofile-lighthouse](https://github.com/user-attachments/assets/72beebb4-2fb0-471f-8e39-b03e2bc63da2)
![character-list-lighthouse](https://github.com/user-attachments/assets/697e8ed3-418e-4616-8dcc-58b9b3d983b0)
![character-editor-lighthouse](https://github.com/user-attachments/assets/741d6dd1-a0e6-49eb-8675-1e5f31fb3dc7)
![character-detail-lighthouse](https://github.com/user-attachments/assets/4eaee4eb-5020-4c09-9518-d50f59aae7e7)
![about-lighthouse](https://github.com/user-attachments/assets/f0208d85-9d3f-4c3a-b500-d98cedbda068)


## Deployment
- **Platform:** The website was deployed to Heroku.
- **High level deployment steps:**
  1. Clone the Github repository.
  2. If running locally, install requirements with `pip install -r requirements.txt`.
  3. Set up a PostgreSQL database for the Heroku environment.
  4. Configure the following environment variables:
      - **DEBUG**, which must be set to FALSE when deploying.
      - **DATABASE_URL**, which should be the URL for connecting to the database instance you have set up.
      - **SECRET_KEY**, which is the SECRET_KEY that Django will use.
      - **CLOUDINARY_CLOUD_NAME**, **CLOUDINARY_API_KEY**, and **CLOUDINARY_API_SECRET**, which must be be obtained via your account on the Cloudinary platform.
      - **OPENAI_API_KEY**, which should be a key for OpenAI's API, obtained through their API platform. If you don't have this, see the environment variable below.
      - **ENABLE_IMAGE_GENERATION**, set this to either TRUE or FALSE. If FALSE, then it will disable all image generation functionality; the backend routes will return an error and the related UI will not be rendered in the frontend.
- **Verification and validation:** I manually tested the deployed site to ensure that it functioned the same as it did in the development environment.
- **Security measures:** All sensitive information was stored in environemnt variables and not committed to the repository. Django debug mode is set according to the DEBUG environment variable (and defaults to FALSE if DEBUG is not set), so as long as the environment variables are correctly configured, debug mode will be disabled when deploying.



## Future Improvements
One feature I didn't get time to implement was generating PDF character sheets for created characters. I was planning to make the character sheets using HTML, and then converting them to a PDF using a solution such as [weasyprint](https://weasyprint.org/).


## Technologies Used
- HTML
- CSS
- JavaScript
- Python
- FontAwesome
- Bootstrap
- AlpineJS
- CropperJS
- Django
- Django AllAuth
- PostgreSQL
- Gunicorn
- Cloudinary for image hosting, along with the `cloudinary` Python library.
- OpenAI API for programmatic image generation, along with the `openai` Python library. 

## Credits
- Unsplash used to source a few images, whilst Dall-E made the rest.
- AI (both ChatGPT and Copilot) was used as a learning aid and to increase velocity throughout. It was also used to generate text content for the site, including Dungeons and Dragons -related flavour text, and to generate characters according to the schema I gave it, which I then populated the database with.  
- I made use of the documentation for the various libraries and frameworks used in the project.
- Google Fonts were used throughout the site.
- [Coolors](https://coolors.co/) was used to help generate the colour palette for the site.
- FontAwesome was used for icons throughout the site, including the icon used in the logo.
- I occasionally used the Code Institute 'I think therefore I blog' walkthrough project as a reference point for certain aspects of Django. 






