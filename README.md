Engineering Plan:  
Frontend Component:  
The frontend component will be written in React. There are three major components to the frontend. First, we have the account creation and authentication page, where a user can create their account and log in. Next, we have the file upload page, where the user can upload a zip file containing their Instagram or Facebook data. Lastly we have the summary slideshow component, which visualizes all the user’s text messaging behavior and compares them with several celebrities.   

The account creation component will consist of a form that prompts a user to input a unique username and a password. It will then make a post request to the backend to create the account and store it in a database.   

The file upload component will accept a file and again, make a post request to the backend. This will send the file, which will parse it as a csv file, then run a number of analysis scripts and ML models that generate the statistics that will be displayed on the frontend.  

The frontend will then make a get request(s) to retrieve the data it will display. Various components will be engineered to contain and display this information. In particular, the main summary component will be a slideshow for each concept we want to visualize. Within each slideshow component, we will have a variety of different layouts. One layout might be a table that shows a list of your top 5 topics to discuss. Another layout might be several columns that illustrate the various texting behavior categories one belongs to. Finally, we will engineer a similarity comparison between the given user and a number of celebrities. This will be displayed as the final slide.   
Backend Component:   
The backend component will consist of a number of data analysis scripts, a component that interacts with a database storing user logins and passwords, as well as select statistics from past user submissions, and also routes that allow the frontend to interact with the backend as an API.   

The data analysis scripts will be written in python because the ease of which dataframes handle large datasets and can be used to train ML models is unparalleled in other languages. A major challenge will be integrating these python components as a cohesive backend as all the projects we have done so far use Java in the backend. However, as there exists Selenium for Python and ways to do routing, this should definitely be possible.   

Interaction with the database will involve queries that search to confirm that a user has entered valid login information, insert and update queries that create a new user or allow for password changes, and also insert and delete queries for storing and removing data collected from a user’s text messaging file.  

One example of this functionality would be finding the percentile in which the user’s response time lies. We would query the database for a sorted list of all user response times, then determine what percent of the times the user is faster than.   

In addition, the backend would need to contain a database of celebrity data so that users could be compared with them and matched in a fun visualization of texting behavior. This would be done by computing the texting behavior based on the celebrity’s Twitter posts, then a similarity score would be calculated using some measure of distance (Euclidean distance, Bloom filter similarity, etc.)  

cleanly break the project into user stories that can be tackled by individual team members. Remember that a “user” needn’t be an end-user of the project! One team member may work to implement functionality where the “user” is another team member. (E.g., “As someone implementing the front-end, I can ask the back-end for data pertaining to…”)  While pair programming is strongly encouraged, everyone should  "own" a non-trivial part of engineering the project.  
User Stories:  
End User:  
I can upload my data to the website as a zip file after downloading it from Instagram or Facebook  
I can view a summary of my data by interacting with a slideshow  
I can make an account with a username and a password  
User can expect their text messaging data to be deleted once they exit the application  
User can interact with the interface to learn specific information about their behavior  
User can share a snapshot of their information with friends  
Frontend Developer:  
I can make get requests to the backend in order to get the statistics to display  
I can make post requests to the backend in order to submit the data for analysis  
I can make post requests to the backend when creating users  

contain a comprehensive testing plan (possibly including automated testing) that will exercise every aspect of your project;  
Thoroughly testing your own code before you try to integrate it with the rest of the program will make everyone’s life much easier.  
Testing Plan:   
Parsing  
Can extract a CSV inputted from a zip file coming from the frontend  
Can clean the CSV data in a way that the analysis can handle it  
Analysis  
Takes a given CSV and returns a JSON of data used for API get requests  
Test models to make sure that they are outputting non-bogus predictions  
Verify that interaction with the database containing stored data is yielding accurate results.  
Frontend  
Test CRUD with backend  
Create a user  
Read user data  
Update user data after submitting a text message CSV  
Delete a user if they want to delete their data  
Automated testing with selenium with uploading a bunch of different text message CSV’s and then making sure that the data displayed on the website is changing after each upload  
Test  

diagrams and/or code contracts for each component, specifications for interfaces between components, and descriptions of major methods and data structures; and  
Code Components:  
Frontend:  
Login Component: the component users will use to log in  
Account Creation Component: the component users use to create an account  
File Upload Component: the component users will use to upload their data file  
Slideshow Main Component: the component housing all the slides  
Slideshow Slide Component: the slide for visualizing a particular concept  
Datatable visualization component: for visualizing statistics represented as a table or rows on the page.  
Columns visualization component: for visualizing statistics represented as columns on the page  
Backend:  
Data analysis components:  
Response Time: gets user response time and which users they respond fastest  
Emoji Usage: what are most popular emojis, which users they send emojis to   
Emotions: what emotions do you communicate the most over text  
Requires a ML model to classify messages by emotion  
Texting Topics: what topics do you discuss most over text  
Requires a ML model to classify messages by topic  
Texting Personality: what is the personality you convey over text  
Requires a ML model to predict each Myers Briggs personality type  
Texting Profile  
Celebrity Comparison  
Uses a distance algorithm to compare user texting behavior with celebrity tweet behavior and output a similarity score.  

a description of how your project might address security or privacy concerns (e.g., GDPR compliance).  
Privacy/Security Concerns:  
This project will have a strong focus on privacy throughout. Since the web application will be taking in private message data, we will be sure to request consent from users. This consent will be free, specific, and informed. The user can also choose to revoke this consent at any point and the analysis will immediately stop.  We will make it clear that their data will not be stored for any longer than necessary. The purpose of the application is to perform analysis upon the data and then return the results of the analysis. It is not to store the data online or sell data to other parties. A user’s data will be private and not accessible to any other party.   

We will also not take any data that is not necessary to perform the analysis. For example, some messaging platforms provide location data associated with messages. Since we are not analyzing this, we will not be using this data at all. We will immediately discard data that is not relevant to our analysis. We will make clear what data we are actually using.   
By April 5th, you should submit a sketch of Part 1 of your specifications document, and you’ll have your first meeting with your project mentor. For our purposes, a sketch is enough to indicate preliminary planning work for your project and allow your mentor to give feedback on those plans. Concretely, integrate your approved outline (with any required modifications) into the standard 0320 specifications format, enumerate a non-exhaustive list of stakeholders, say how you will start gathering user requirements, and fill in a couple draft user stories to illustrate how you are thinking about your project.  

Note that this first mentor meeting coincides with the start of Sprint 4, but you will not have a Sprint 4 mentor meeting yet.  

Fill out the “Specifications Sketch” block under the “Tasks” table and submit a Weekly Mentor Meeting Form before you meet with your mentor TA — fill in the Code Review with “n/a”.  


Preliminary Planning Work:  
Frontend:  

Tasks  
Design Frontend in Figma  
Set up react app  
Design frontend with placeholder components  

Then fill in the placeholder components with returned data from API calls  
User login/storing the data between uses? Just only store the results  
Potentially super costly in terms of storage space  
Prompt for user data input  
Personality analysis, sentiment/emotion, emoji usage, response time, # texts sent, who you talk to the most - each one will require its own frontend component to display to user  




Backend  
Tasks:  
Data collection:  
Data cleaning/parsing:  
Extract text messages from user’s phone  
Clean data for entry into models/analysis frameworks  
Data Analysis:  
- statistical analysis of text messages and behavior   
- NLP type analysis of text messages using pre-trained models  
- Use VADER library for functionality  
API creation:  
Frontend can pass in the user data in order to get the full set of stats/analysis performed on the user’s text messages  


Find API that gets the data easiest so messenger, twitter, or instagram  
Recommendation similar to other users from like twitter or something  

Section 1:  Introduction  
1.1 Project Specific Details   

Answer these questions:  
Spotify Wrapped for Text Messages  
Alex Bao, Suraj Anand, David Grossman, Om Naphade, Vignesh Pandiarajan, Neil Xu  
1.2 Purpose   
The goal of this project is to take a user’s text messaging data, analyze it, and present them with an interactive page that details metrics and information surrounding their texting habits. For instance, we may examine how frequently an individual uses emojis, their most frequently discussed topics, the user’s personality, etc. We plan to use a combination of statistical analysis, machine learning, and frontend design to create a compelling user experience.  

Text messaging is one of the most frequently used modes of communication in the modern world, yet many people likely do not have a clear understanding of how their text messaging behavior is perceived by or affects others. We are attempting to provide users with information regarding their texting behavior in order for them to make more informed choices and decisions surrounding how they interact with others online.  

We will gather knowledge about the problem through a survey that we will distribute to individuals querying them about their interest in learning about their messaging behavior.  

Users of text messaging platforms are impacted by this problem as it is their information that we are analyzing. Furthermore, by seeing a visualization of their text messaging behavior, users may be inclined to change their texting behavior, clearly impacting this group in some way.  

An individual’s contacts could be impacted if the user decides to change their messaging behavior. For instance, a user who dislikes the fact that they tend to convey sadness frequently over text may shift to conveying more positive messages. This would very much change the nature of certain conversations over text.  

1.3 Intended Audience and Intended Use   
In this section you’ll outline who will ultimately use your product, and therefore whose desires, concerns, and feedback will be central to your design and development process.  
Answer these questions:  
Who are your intended end-users?  
What parameters define the space of potential users and how did you choose the “values” of those parameters? For the recipe app, for instance, I might choose: people with low skill level, interested in Southeast Asian cuisine, with busy lives (so little time to cook).  
Obviously, if your app is public, some people outside your intended audience may use it. Try to address that concern in this section.  
How will the app fit into the lives of your users?  
How often will they use it?  
Is it for personal use or professional use?  
1.4 External Stakeholders   
Here you’ll discuss any stakeholders who likely won’t directly use or support the development of your app. Please list at least three groups, including one who will likely either oppose your project or may be harmed by it. Non-user stakeholders are important to consider especially when they will not receive direct compensation or benefit from your project and/or may be hurt by your project.  
Examples for my recipe app: competitors (cookbooks, other cooking apps); food vendors; experts (could include community members) I consult for recipe information  
Text messaging users  
Apple  
Facebook/other messaging platforms  
Text messaging users may both support and oppose the project as they are the main consumers while also being the ones who are most likely to be harmed by the project. Text messaging users do not have the agency to deny being used for data collection as their friend or someone they texted could submit the data and thus the user’s data would be used unbeknownst to them. This aspect of the data collection process could lead to strong opposition from users and figuring out a way to anonymize and safely handle the data is a main priority  
Apple is a major stakeholder in this project as we will be using data from their iMessage service as it is a platform where we could easily get a user’s text information. However, as our project mainly revolves around Apple and its products, Apple may oppose such an idea as the privacy issues surrounding the data collection may infringe upon Apple’s user privacy agreements.   
Other messaging platforms are also stakeholders as their users would not be able to use this project since we do not intend to enable the collection of user texts from other platforms for the scope of this final project. As other platform users would not be able to use the product, if the Wrapped for Texts project were to become popular, other platforms may be negatively affected as users may be more inclined to use the iMessage service.   

Answer these questions:  
For each of the groups you mention, how might they respond to your project?  
For stakeholders who might oppose or be harmed by your project, how and why? How can you mitigate harm and conflict?  
Are there ways you can compensate external stakeholders you interview or who otherwise assist you?  
1.5 Scope and User Stories   
In this section, you’ll clearly define your product’s scope, setting guardrails to prevent taking on too much. You’ll do this by detailing the “user stories” your product will fulfill (i.e., the general pieces of functionality your app provides, phrased as “a user can do/access/create/etc. ____”). You’ll also detail some user stories you’re not planning on implementing. It’s better to plan to complete too few features than too many.  
Answer these questions:  
What are you not planning on implementing?  
What are some features you’ve thought of that are outside your project scope? You can always implement these if you have time, but set them aside for now. At least you’ve written them down, and can come back to them later.  
What are your app's user stories?  
Avoid going into detail. Instead, list things like “user can create and log into a personal account” or “user can search for and save recipes.”  

User can upload their text messaging data using a zip file as input to analysis  
User can obtain a visualization of their text messaging behavior   
User can expect their text messaging data to be deleted once they exit the application  
User can interact with the interface to learn specific information about their behavior  
User can share a snapshot of their information with friends  
Time restricting:  
User can login and access their past submissions and analytics  
More complex models to analyze user   
Not implementing:  
User messaging handling from other platforms such as instagram and facebook  
No implementation of DL models that we might need to train ourselves.  
1.6 Definitions and Acronyms   
Your design process may require defining new terms or acronyms. For instance, you might have specific names for different kinds/tiers of user; you’ll specify those definitions here. This section is mostly for your benefit, allowing you to use your own domain-specific language in the rest of the document.  
Wrapped–means summarized in our context  

Section 2: Overall Description  
2.1 User Needs   
This section will reference any user research you’ve done and the requirements you’ve gathered. User research might involve interviews, general research, or consulting experts. From your research, you should gather a list of concrete needs your intended audience has and how your product will help address those needs.  
Researching user needs is a great opportunity to confirm that your product solves an existing and significant problem. For that reason, never ask leading questions (e.g., “How do you usually find recipes for cooking? Would you be interested in using an app for that?”). This will bias user answers toward confirming your research goals. Better to realize you’re fulfilling a non-existent or insignificant need before starting a project than after putting hundreds of hours of work into it.  
Answer these questions (and feel free to use them when interviewing:  
What are the most important tasks your users have to perform in the context of your product? (E.g., for my recipe app, maybe it’s finding an appropriate recipe based on ingredients and finding time to cook)  
What are the biggest gaps in current tools used by your users? (E.g., cookbooks don’t have sophisticated search functionality)  
What general feelings do users express about the problem you’re working on? (E.g., people express frustration at how long it takes to find an appropriate recipe)  
How often do users perform tasks in the context of your project (i.e., how often will they use the product)?  
In what context will users interact with your product? At work? At home? In school? Some combination?  
Are there secondary users? Do they have different needs? (E.g., makers of medical devices need to know the needs of doctors as well as the needs of their patients)  
Separate from user research: can you think of any ways your app might create user needs that didn’t exist before? (E.g., the addictiveness of many social media apps creates a “need” that didn’t exist before)  
This doesn’t necessarily disqualify your app, but is something you should think about!  
Any other useful information that doesn’t fit into these questions.  
2.2 Assumptions and dependencies  
In this section, you’ll outline the assumptions—both technical and non-technical—you’re making in designing your project.  
Answer these questions:  
What software and other technology does your project rely on?  
Particularly when working with web technologies, you can expect dependencies to change frequently and for functions to become deprecated. This won’t necessarily break your project, but might! In the context of this class, that likely won’t happen, but this is good practice for future long-term projects.  
What non-technical dependencies does your project rely on?  
Are you relying on the legality of collecting certain data from your users?  
Does the relevance of your app rely on a social and/or cultural context? (E.g., a Squid Game-themed app)  
What normative assumptions are you making?  
Are you choosing to center a particular user group over others? Why?  
What assumptions are you making in claiming that your app adds value to people’s lives?  
You don’t necessarily need to justify these assumptions, but sometimes stating them will make you realize you disagree with them slightly.  
Financial dependencies  
Based on the dependencies enumerated above, what are the financial needs for development of your project (broadly speaking)? You don’t need exact numbers, especially for the purposes of this class, but are there services or technologies you’ll need to pay for? You shouldn’t have to pay for anything in this class, but maybe there are external APIs that have a paid tier you’d like to use eventually after the class is over.  
Section 3: System Features and Requirements  
3.1 Risks   
The main risks in this project are with data privacy. Since the application needs text data to perform the analysis, we will be taking in a lot of sen	  
This section is one of the most important in your specification. In it you’ll identify the key risks your app creates for users, external stakeholders, and your project itself. Make sure to specify when you deem risks necessary. We are not judging you on your failure to overcome certain risks, especially ones involving a larger social, economic, and political context. We simply want you to be aware of them!  
Answer these questions:  
Stakeholder risks (all entities who use or are affected by the app)  
How might data used for decision-making within your app result in unfair outcomes for certain users or stakeholders?  
Decision making within our app includes the analysis of texts submitted by users. Outcomes for different users will purely reflect the data they entered which would result in different though not necessarily unfair outcomes for each user.   

Which features of the represented groups do your app’s data not represent?  
The summary of texts will only include a small subset of potential analysis which means that a lot of the potential features of users for the app will not be represented.  

What limitations exist on stakeholders’ ability to manipulate the data relevant to them?  
Stakeholders must be able to download the data from their social media/messaging platform of choice and then upload the data to the site for analysis. Since the data is user generated texts so they have full agency over the data that they create and upload.  

Does the app benefit one group of stakeholders more than others?   
This app would be designed to only support data from one or two platforms which means that users of other platforms would not be able to use the app. Additionally this app benefits frequent texters more than those who text less as having more data would provide better analysis.  

Which data are publicly accessible?  
Aside from the average response rate, used to show what percentile a user is in terms of response time, no data will be publicly available and user uploaded text message data will be converted into a short list of values and the data will be deleted from the app.  

Is data ever harvested or used without stakeholder consent?  
There will not be any cookies or data harvesting without stakeholder consent. The uploading process is completely dependent on the stakeholder and the data privacy related information will be presented upfront before uploading.  

Are there situations when a stakeholder cannot inspect how your app came to a decision relevant to them?  
The app is predicated on a black box algorithm for sentiment analysis, stakeholders will not be able to inspect how our app came to a decision relevant to them. However, the methodology to generate the analysis will be publicly available and provide a detailed explanation as to how the algorithm arrives at each decision.  

Does your app disrupt community wellbeing in any way, such as undermining trust, communication, or participation?  
The app is designed to only display relevant information for a given user. Users could share who they most frequently interact with, which may undermine trust if two users assume they were each other's most frequently interacted with users. However, that disruption only occurs when users go out of their way to share information and the likelihood of such issues seems low.  

Does your app make inefficient or unnecessary uses of resources and/or energy?  
The app uses a pretrained model which should cut down on the amount of resources and energy used. However, user data must be recalculated each time they upload a file as the text messaging data is never stored. While this cuts down on the amount of energy used to store data, there will be an increase in energy usage for analysis though to some extent, the analysis energy consumption can not be avoided.  

External risks  
How does your app fit into its social, economic, and political context? Does it actively work against systems of oppression (racism, sexism, classism)? How?  
In an age where data privacy is a hot button topic, this app supports user data privacy as it is predicated on users uploading their own data as well as not storing the data. However, the app does little to fight against racism, sexism, or classism. The app may also perpetuate biases that exist in this system as it will use a pretrained sentiment analysis model.  

Does your app rely on services that participate in labor exploitation or create environmental harms?  
The app does rely on a pretrained model which contributed to environmental harm to train, however, this is a necessary evil as it saves additional training on our end which would further contribute to environmental harm.   
3.2 Data Requirements   
In this section, you’ll specify which data you need to collect from your users and other stakeholders, and whether you’ll store, use, or store and use the data.  
For each datum, answer these questions:  
If you only plan on storing this datum, not using it, why?  
If you plan on using this datum, what function does it fulfill?  
What process of consent, if any, do you provide your user when collecting this data from them? If you don’t provide one, why?  

As discussed earlier, we will actually be collecting a significant amount of information from our users. We will be collecting messaging data, which will include text, time, recipient and sender. This can potentially be sensitive information, so we will be very careful with it. We will be sharing this information for the purpose of the analysis. After that, we will delete the data and only keep the results of the analysis. This will then be shown to the user. The user can also login at any time and then see the results of their analysis again. We will be sure to ask the user for consent. Uploading their data is totally voluntary. They will be informed that their data will be deleted after the analysis and they can choose to save their analysis or delete it from the server.   


3.3 System Features   
This section will change as you develop your project. You should write down your initial design before writing any code, and then come back and fill in the details when you’ve implemented your features.  
In this section you’ll define the categories of functional requirements. This is subtly different from user stories: rather than defining what the user can do, you’ll define the high-level organization of your software components. The former is user-facing, while the latter is developer-facing.  
Consider the following:  
What high-level modules define the functionality of your app?  
How will you separate your code into these separate modules?   
How will modules communicate with each other?  
How will you make modules reusable and generic when necessary?  
Are there any known bugs in your program?  
How to build and run your program?  
These are also defined in our functional requirements to some extent, but they are worth restating.   
The main modules are:  
Login  
Frontend component in which user will input a username and password  
Backend will store usernames and passwords, with hashing function obviously  
Once authenticated, they will be able to access their analysis  
Data Upload:  
Frontend component where one can upload their data  
Backend component where data will then be stored in a database  
CSV Parser:  
Backend component only, data will be parsed and then analyzed  
Analysis Scripts:  
Analysis done in python, using sci-kit to do the analysis  
Vectorization of the data  
API Communication:  
Setup APIs for username and password between backend and frontend  
Setup APIs for sending results of analysis from backend SQL database to frontend  
Data Visualizations:  
Frontend component, set up different sections where one can see specific parts of their analysis  

End User:  
I can upload my data to the website as a zip file after downloading it from Instagram or Facebook  
I can view a summary of my data by interacting with a slideshow  
I can make an account with a username and a password  
User can expect their text messaging data to be deleted once they exit the application  
User can interact with the interface to learn specific information about their behavior  
User can share a snapshot of their information with friends  
Frontend Developer:  
I can make get requests to the backend in order to get the statistics to display  
I can make post requests to the backend in order to submit the data for analysis  
I can make post requests to the backend when creating users  


3.4 Functional Requirements   
This section will change as you develop your project. You should write down your initial design before writing any code, and then come back and fill in the details when you’ve implemented your features.  
In this section you’ll describe the modules (i.e., pieces) of your program that define the different feature requirements for your project. You can use your user stories to guide you, defining software components that will combine to fulfill each user story. This section will likely be the most extensive.  
Answer these questions for each requirement:  
When during the user flow should this component be available?  
How does this component interface with the rest of the app?  
Does it collect user input directly? Does it communicate with other components? External APIs? Backend database?  
Are there security measures to prevent all but certain components from accessing it?  
How does it process data?  
Algorithms, data structures, etc   
Frontend:  
Login Component: This component will be another React component that handles login and account creation. Logging in will send a post request that will verify that the username and password are valid. Creating an account will verify that the username is unique and send a post request to insert the new account into the database.  
Data Submission: We will include a component in which users can select a file that they want to submit. This component will be created in React and will send a post request containing the file to the backend for parsing and analysis. The returned object will contain all the necessary data for the visualization component to be created. Once the visualization has been created, the user’s csv file will be deleted, and only the numerical values computed will be stored in the database. This ensures that the user’s text messages will not be leaked or used for malicious purposes. Furthermore, having the authentication system ensures that only a user can see what their true results are.   
Backend:   
The component that handles CSV parsing will need to first extract the csv containing all the messages the user has sent. It must then ensure that the table names and column names are compatible with the data analysis scripts.  
The analysis scripts process data using a variety of algorithms that compute the user’s average response time, their most frequently used emojis and other metrics. Furthermore, we implement a number of machine learning models that will classify text messages based on emotion, topic, personality, etc. These models will use the sklearn package to fit a naive bayes, linear svc, or other classification model to a set of training data found on Kaggle. The results of these predictions will then be aggregated and used to display some visualization to the user.  
In order to communicate with the database, we will need to write a number of SQL queries that will get the data we need to analyze, insert new data, and update existing data. An SQL query may return a list of all the average response times all users have submitted. We can then find what percentage of users a user’s response time is faster than.  
3.5 Testing Plan   
In this section you’ll outline your plan for testing your app. You don’t need to detail specific test cases, but you should give a high level description of which features and potential bugs you want to test. You can use the functional requirements you outlined to structure this section.   
Parsing  
[SYSTEM] Can extract a CSV inputted from a zip file coming from the frontend  
[SYSTEM] Can clean the CSV data in a way that the analysis can handle it  
Analysis  
[SYSTEM] Takes a given CSV and returns a JSON of data used for API get requests  
[UNIT] Test models to make sure that they are outputting non-bogus predictions  
[UNIT] Test that each analysis script performs on edge cases and returns accurate information  
[UNIT/SYSTEM] Verify that interaction with the database containing stored data is yielding accurate results.  
Frontend  
[SYSTEM] Test CRUD with backend (likely using Selenium)   
Create a user  
Read user data  
Update user data after submitting a text message CSV  
Delete a user if they want to delete their data  
Automated testing with selenium with uploading a bunch of different text message CSV’s and then making sure that the data displayed on the website is changing after each upload  

Include instructions on how to run tests from the command line!  
3.6 External Interface Requirements  
In this section you’ll define how your app will interact with the “outside world,” including the user.  
Answer these questions:  
How will your user interact with your app? Specifically, how will you make it accessible to visually, motor, cognitive, or otherwise impaired users?  

Users will be able to interact with our app on a frontend where they can submit a zip file containing their messaging data. We will make this aspect compatible with a screen reader so they can still use it to submit data.  

Users will interact with a colorful slideshow displaying their usage behavior. We will make this accessible by checking that our color contrast is high enough for colorblind users to view.  

If applicable, how will your app communicate with external software?  
This will likely include your database, since you probably won’t want to host it locally, but rather on a service like Google Cloud Platform or Firebase.  
Our app will communicate with a database hosted externally in order to store the analysis results related to a given user, but not their actual text messaging data. This database will be an SQLITE database which we will query from the backend. The frontend is able to interact with the backend by making get and post requests in order to send and receive the data.  
3.7 Non-functional Requirements  
Almost done! This last section will outline more ~nebulous~ requirements.  
Answer these questions:  
What standards of performance must your product meet?   
Speed? Reliability?  

A high standard of speed should be met because users who wait too long for their results to load might lose interest and navigate away from the page.   

A high standard of reliability should also be reached because failures to load the data will result in incomplete or inaccurate information on the user’s end. This could result in misleading visualizations that misinform a user about their texting behavior.  

What standards of security must your product meet?  

Our product must maintain high levels of security because leaking a user's texting information could lead to pretty serious consequences if they sent any personal or sensitive information on that platform. In order to maintain this security, we have implemented an authentication system and make sure to delete the csv containing the user’s messages once the analysis scripts have been run.  

What standards of privacy must your product meet?  

Our product should ensure that users can never be identified and that their data will be secure and not leaked. Users can guarantee that with the authentication system, no one else will be able to view their results, and that their text data will be deleted after they exit the product.  

How “flashy” and aesthetically pleasing does your UI need to be?  

We want our UI to be flashy in a subtle way, but overall very aesthetically pleasing because it is intended to visualize a set of data in a fun way and also keep users engaged so that they are willing to share our product with their friends and family.  

How accessible does your UI need to be?  

Our UI will need to be accessible for users who are hard of sight or colorblind. We should ensure that color contrast is high enough for colorblind users to interpret and interact with our graphs and statistics. Furthermore, our HTML should be clean and laid out such that screen readers are compatible with our product.   




