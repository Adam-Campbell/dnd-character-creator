# The Adventurer's Rest

## Overview

### Purpose
The Adventurer's Rest is an online Dungeons & Dragons character creation and management tool. It provides an intuitive interface for creating a character conforming to the subset of Dungeons and Dragons rules contained within 
the [Systems Reference Document](https://www.dndbeyond.com/resources/1781-systems-reference-document-srd?srsltid=AfmBOooY4RPy4pqzFizxz7M8g6XqFSs6ig6Iiy24rGq_g1TwqeZZatup).
It also provides an online character sheet, displaying the character's details in an easy-to-digest layout.


### Target Audience
The target audience for this website is Dungeons & Dragons players (current or prospective) that are looking for an easy way to manage their Dungeons & Dragons characters. The site gives them a simple way to create, store and share
their characters, as well as to browse other users characters for inspiration.

![responsive-about-page](https://github.com/user-attachments/assets/cf009579-a035-486f-be83-2a5fdd1371bd)

[Link to deployed site](https://dnd-character-creator-196a1c69fe18.herokuapp.com/)

## User Stories

### Must-Have User Stories
- **User Story 1:** As a user I can create an account so that I can store my created characters online.  
  **Acceptance Criteria:**
  - The user can sign up or log in using a username and password
  - The signup and login pages are styled to match the rest of the site
  - The users login status is reflected in the sites header
- **User Story 2:** As a user I can create a character and save it to my account so that I can reference it again later.  
  **Acceptance Criteria:**
  - A logged in user can create a character using an intuitive UI.
  - The character is saved to the users account
  - Validation is performed on the front end and back end, for a better user experience
- **User Story 3:** As a user I can edit my previously characters so that I can update it with my new ideas.  
  **Acceptance Criteria:**
  - A logged in user can load up one of their previously made characters in the character creator/editor, and make changes to that character.
  - Upon saving, the correct character entity in the database will be updates with the new details.
- **User Story 4:** As a user I can view the character sheet for a character so that I can see the information presented in an easy-to-digest manner.  
  **Acceptance Criteria:**
  - Character sheet presents the character information in a clear way.
  - Character sheet is responsive.
- **User Story 5:** As a user I can browse through all public characters so that I can draw inspiration from the creations of others.  
  **Acceptance Criteria:**
  - User can view a paginated list of character cards for publicly viewable characters.
  - User can apply filters and ordering to the list.
  - If user clicks any of the character cards then they are taken to the corresponding character sheet
- **User Story 6:** As a user I can have a profile page so that I can display my public characters, and write a bit about myself.  
  **Acceptance Criteria:**
  - Each user has their own profile page
  - It can only be edited by the correct user
  - Other users will see the users basic information and public characters, whilst the user themselves will see everything.
- **User Story 7:** As a user I can delete any of my previously created characters so that I can control what remains online.  
  **Acceptance Criteria:**
  - User is presented with the option to delete any character that they have created.
  - Deletion can be triggered from the character sheet.
  - User is asked to confirm before deletion occurs.
  - User cannot delete any characters that they did not create.
- **User Story 8:** As a prospective user I can view the homepage so that I can determine whether I want to use the site.  
  **Acceptance Criteria:**
  - There is a homepage served at the base route
  - The homepage is informative
  - The homepage is responsive

### Should-Have User Stories
- **User Story 1:** Briefly describe the should-have feature.  
  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.
- **User Story 2:** Briefly describe the should-have feature.  
  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.

(Include all prioritized should-have features)  
**Guidance:** Document the secondary features that you aim to implement in Phase 3: Should User Stories Implementation & Any Advanced Features. Include clear acceptance criteria for each.

### Could-Have User Stories
- **User Story 1:** Briefly describe the could-have feature.  
  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.
- **User Story 2:** Briefly describe the could-have feature.  
  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.

(Include any could-have features considered for future enhancements)  
**Guidance:** Document any optional features that are nice to have but not essential.

## Design Decisions

### Wireframes
Include wireframes for key sections of your website.  
Briefly describe the design choices, including layout, colour schemes, and fonts.  
**Guidance:** Start this section during Phase 1: Ideation & Initial Setup and update it throughout Phase 2 and Phase 3. Include digital wireframes created in Phase 1. Document the reasoning behind your layout choices, colour schemes, and font selections.

### Accessibility Considerations
Discuss how accessibility guidelines were adhered to, including colour contrast and alt text for images.  
**Guidance:** Outline how you've incorporated accessibility into your design, ensuring that your project adheres to guidelines such as WCAG.

## AI Tools Usage

### DALL-E
Describe how DALL-E was used for image generation, including examples of successes and challenges.  
**Guidance:** Specifically mention how you used DALL-E for image generation and the impact this had on your design process.

## Features Implementation

### Core Features (Must-Haves)
- **Feature 1:** Description of the implemented feature.
- **Feature 2:** Description of the implemented feature.

(Include all must-have features)  
**Guidance:** Use this section as you complete Phase 2: Must User Stories Implementation & Testing. Document all the must-have features you implemented, explaining how they align with the user stories and acceptance criteria.

### Advanced Features (Should-Haves)
- **Feature 1:** Description of the implemented feature.
- **Feature 2:** Description of the implemented feature.

(Include all should-have features)  
**Guidance:** Include any advanced features you implemented during Phase 3: Should User Stories Implementation & Any Advanced Features. Explain how these features enhance user experience and their alignment with the acceptance criteria.

### Optional Features (Could-Haves)
- **Feature 1:** Description of the implemented feature (if any).
- **Feature 2:** Description of the implemented feature (if any).

(Include any could-have features that were implemented or considered)  
**Guidance:** If any could-have features were implemented, describe them here. This is an opportunity to showcase extra work done beyond the initial scope. But remember - keep it simple! Focus on the Must stories first. Could user story features are commonly earmarked for future project iterations.

## AI Tools Usage

### GitHub Copilot
Describe how GitHub Copilot assisted in coding, including any challenges or adjustments needed.  
**Guidance:** Reflect on how GitHub Copilot assisted in coding, particularly any challenges or adjustments that were needed to align with project goals.

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
