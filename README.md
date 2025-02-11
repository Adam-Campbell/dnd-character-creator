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


## Deploymant

TBD


## AI Implementation and Orchestration






## Testing and Validation

### Testing Results
Summarize the results of testing across different devices and screen sizes.  
Mention any issues found and how they were resolved.  
**Guidance:** Summarize the results of your testing across various devices using tools like Chrome DevTools, as outlined in Phase 2. Mention any issues found and how they were resolved.

### Validation
Discuss the validation process for HTML and CSS using W3C and Jigsaw validators.  
Include the results of the validation process.  
**Guidance:** Document your use of W3C and Jigsaw validators to ensure your HTML and CSS meet web standards. Include any errors or warnings encountered and how they were resolved.

## AI Tools Usage

### GitHub Copilot
Brief reflection on the effectiveness of using AI tools for debugging and validation.  
**Guidance:** Reflect on how GitHub Copilot assisted with debugging and validation, particularly any issues it helped resolve.

## Deployment

### Deployment Process
Briefly describe the deployment process to GitHub Pages or another cloud platform.  
Mention any specific challenges encountered during deployment.  
**Guidance:** Describe the steps you took to deploy your website during Phase 4: Final Testing, Debugging & Deployment, including any challenges encountered.

## AI Tools Usage

### Reflection
Describe the role AI tools played in the deployment process, including any benefits or challenges.  
**Guidance:** Reflect on how AI tools assisted with the deployment process, particularly how they streamlined any tasks or presented challenges.

## Reflection on Development Process

### Successes
Effective use of AI tools, including GitHub Copilot and DALL-E, and how they contributed to the development process.

### Challenges
Describe any challenges faced when integrating AI-generated content and how they were addressed.

### Final Thoughts
Provide any additional insights gained during the project and thoughts on the overall process.  
**Guidance:** Begin drafting reflections during Phase 1 and update throughout the project. Finalize this section after Phase 4. Highlight successes and challenges, particularly regarding the use of AI tools, and provide overall insights into the project.

## Code Attribution
Properly attribute any external code sources used in the project (excluding GitHub Copilot-generated code).  
**Guidance:** Document any external code sources used throughout the entire project, especially during Phase 2 and Phase 3. Exclude GitHub Copilot-generated code from attribution.

## Future Improvements
Briefly discuss potential future improvements or features that could be added to the project.  
**Guidance:** Reflect on potential enhancements that could be made to the project after Phase 4: Final Testing, Debugging & Deployment. These could be Could user story features you didn’t have time to implement or improvements based on testing feedback.
