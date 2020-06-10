# Synthetic Synesthesia: From Handwritten Text to Colorful Design

DSC160 Data Science and the Arts - Final Project - Generative Arts - Spring 2020

Project Team Members: 
- Mariam Qader, maqader@ucsd.edu
- Molly Rowland, mhrowlan@ucsd.edu
- Myra Haider, myhaider@ucsd.edu
- Enrique Sanchez, ens004@ucsd.edu
- Alexandria Kim, aek005@ucsd.edu

## Abstract

For our generative art project, we are interested in the condition synesthesia. This is the condition where a person’s senses are mixed, such as tasting color, or hearing textures. It affects “at least 4% of the population” of the US and there are more than 50 forms of synesthesia (Wu). Grapheme-color synesthesia is the specific condition in which people experience colors when thinking about letters, numbers or words (Simner & bain). One way to help others understand this condition, is by using generative art methods to create synthetic synesthesia for those who don’t have the condition. 

We plan to make a neural network to transform text to color. Many of the articles we found on this subject discuss using GAN to create the deep learning model. One of the papers discusses taking a database of handwritten characters, implemented as a multilayer convolutional neural network, and having a separate multilayer convolutional neural network to create a colored version of the text based on a grapheme-color synesthetes (Bock). From this example, we hope to create our own responsive model.

Our plan is to build a text recognition system and create a model that outputs a colored visual of a word. The user can input a word of their choice, and our model will output the word containing the colors associated with the letters in the word (e.g. https://synesthesia.me/see-your-name). The user will draw a word of their choice and then upload this image to our model. Our model, trained on names of objects, will then determine what word was written and translate it to text.

Our goal is to make an interactive widget through Python libraries like Holoviz that will produce a jpg image of colors file based on the user inputed handwritten text. Some challenges that may arise while working on this project include training the text recognition system to accurately determine the words. We may have to create some parameters as to what words are acceptable to input (i.e. maximum length of 10 letters).

Through our project we hope to take both the technical and qualitative skills we have been shown in class and apply them to our area of interest. We will be using GAN to implement our project to help us gain a greater understanding of synthesia and how it affects the people around us. Many of the example projects shown in class help us understand different people and cultures through technology, which is exactly what we hope to achieve here. Synesthesia is an interesting condition to study as it provides insight into how the brain perceives things. It gives us a chance to see how people with this condition perceive the world, and helps us understand how the world can look very different to everyone. This project will also allow us to learn more about the condition, and the effects it has on different people. 

**Works Cited**
- Bock, Joel R. “A Deep Learning Model of Perception in Color-Letter Synesthesia.” 2017, doi:10.20944/preprints201712.0128.v1.
- Laken, Paul van der. “Neural Synesthesia: GAN AI Dreaming of Music.” Paulvanderlaken.com, 30 Oct. 2019, paulvanderlaken.com/2019/10/29/neural-synthesia-gan-ai-dreaming-of-music/.
- “Type Your Name.” What Color Is Your Name?, synesthesia.me/see-your-name.
- Wu, Jun. “Synesthesia, An Inspiring Condition For AI Researchers.” Medium, Towards Data Science, 27 Jan. 2020, towardsdatascience.com/synesthesia-an-inspiring-condition-for-ai-researchers-10cd57708855.
- Simner, Julia, and Angela E. Bain. “A Longitudinal Study of Grapheme-Color Synesthesia in Childhood: 6/7 Years to 10/11 Years.” Frontiers, Frontiers, 4 Sept. 2013, www.frontiersin.org/articles/10.3389/fnhum.2013.00603/full.

## Data and Model

(10 points) 

Our project utilizes libraries to make our project interactive with users. We used Holoviz and Ingestion libraries to create user generated text in a notebook, and save that image into our handwritten text recognition’s systems data directory. 
In trying to create our predictor we began with doing some initial research. We were able to acquire a git repository with the code for a Handwritten Text Recognition System that utilizes TensorFlow. This code was published by Harald Scheidl in an article on Towards Data Science. The model uses a neural network to do word recognition. It takes an input image of width 128 and height 32, and passes it into convolutional neural network (CNN) layers, recurrent neural network (RNN) layers, and then uses Connectionist Temporal Classification (CTC) to decode the handwritten word into a string. The CNN layers are trained to extract the features of the letters through a 5 layer unit. The layers add channels to the output feature map of size 32x256 before calling the RNN. Inside the RNN, relevant information is propagated through the pipeline to create a matrix of size 32x80. This output matrix is passed into the CTC which computes the ground truth text and the loss value. The CTC decodes the matrix into the final text returned as a string.  This model has been trained on data from the IAM Handwriting data database from FKI: Research Group on Computer Vision and Artificial Intelligence out of the University of Bern in Switzerland.
In this model, Tensorflow is used. One of the most difficult parts of using this code was that the tensorflow library it had been implemented with was outdated. The first step in using this code was going through the different files in the model and updating the code to the proper tensorflow imports. The model is broken into four components: Sample Processing, Data Loading, the Model, and a main file to execute all the steps together. The sample processor prepares the image dataset for the neural network while the data loader reads the samples, putting them into batches for the model to be trained on. The model file can be used for both training and inference, and the main method calls all the files to produce the recognized string a confidence score. We found that the model works best on common words, which has to do with the data it was trained on. Despite this, the model still has the ability to identify unknown words as it is trained to look at both the single letter and the combination of likely letters surrounding individual characters to predict the word. 
After the Handwriting system processes the under inputted text, it is passed into our synthetic synesthesia art creator. In this part of the generative process, we break down the recognized text from the first part of the model into individual characters and associate a color to each letter. This is done by using the most common color associated with each character by synesthesia patients, so we can get a sense of the colors a typical person with synesthesia may see. To generate the art, we use the turtle package in python to draw colorful geometric shapes that can show the user the synesthesia colors is an aesthetically pleasing way. We have three different outputs which are randomly chosen from for each instance of a word.

The data we used for associating colors to letters is found within the article A Deep Learning Model of Perception in Color-Letter Synesthesia by Joel R Bock. This researcher also looked into creating a net to associate handwriting to common synesthesia colors. He was able to identify the most common colors a synesthesia patient may see for each letter. 


**User Handwritten Text:** Image of handwritten text that is created by the user and passed into the text recognition model.

## Code

Run the [Synesthesia_Tool.ipynb](src/Synesthesia_Tool.ipynb) notebook to use the final tool and generate your own results. For best performance, please run the noteook **locally** as the generation of the final visualization is both faster and nicer when compared to Datahub.

**Data Acquisition/Preprocessing**

[ingestion.py](src/ingestion.py): Script that enables the user to hand write their own text, save it, and upload it into the text recognition model. Resizes and manipulates the image autamitcally to conform to model requirements. Widgets are made available through the Holoviz and Bokeh Python libraries.

**Generative**

[draw.py](src/draw.py): Draws visualizations using a series of inputted colors. Uses the Turtle and Mobilechelonian Python libraries to draw the visualzations locally and on Datahub, respectively.

**Model**

[main.py](src/main.py): Main script. Runs text recognition model on image and produces a visualization.

Other Python scripts and files: Borrowed code for text recognition neural network generation.


(20 points)

This section will link to the various code for your project (stored within this repository). Your code should be executable on datahub, should we choose to replicate your result. This includes code for: 

- code for data acquisition/scraping
- code for preprocessing
- training code (if appropriate)
- generative methods

Link each of these items to your .ipynb or .py files within this seection, and provide a brief explanation of what the code does. Reading this section we should have a sense of how to run your code.

## Results

**Example: coffee**

<img src=results/inputs/coffee_input.png width=300>

Output: 

<img src=results/outputs/coffee_output.png width=460>

<img src=results/outputs/coffee_visual.png width=300>

This specific input had a probability of 0.63 of describing the word “coffee”. The word “coffee” resulted in a hexagram-spiral containing the colors: yellow, white, and green.

**Example: tools**

<img src=results/inputs/tools_input.png width=300>

Output:

<img src=results/outputs/tools_output.png width=425>

<img src=results/outputs/tools_visual.png width=300>

This specific input had a probability of 0.91 of describing the word “tools”. The word “tools” resulted in a color wheel containing the colors: blue, white, and yellow.
 
**Example: covid**

<img src=results/inputs/covid_input.png width=300>

Output:

<img src=results/outputs/covid_output.png width=425>

<img src=results/outputs/covid_visual.png width=300>

This specific input had a probability of 0.89 of describing the word “covid”. The word “covid” resulted in a hexagram-spiral containing the colors: yellow, white, purple, and blue.
 
**Example: DSC**

<img src=results/inputs/DSC_input.png width=300>

Output:

<img src=results/outputs/DSC_output.png width=300>

<img src=results/outputs/DSC_visual.png width=300>

Our model recognized this specific input as the word “1sC” with a probability of only 0.05. This is probably due to the fact that our text recognition model is trained on the names of objects. Since DSC is an acronym and not an actual word on its own, our model has a harder time translating the handwritten text. Due to this, we added numbers to our color dictionary in case our system mislabelled any handwritten letters as numbers. The word “1sC” resulted in a spirograph containing the colors: maroon and yellow.

As our text recognition system was trained on names of objects, our results are most accurate when inputted with objects or words verses acronyms or names. The final visual output encapsulates the word as a whole, randomly choosing colored lines based on the color associations of each letter in the word. The shape of the output is also randomly chosen between a hexagram-spiral, spirograph, or a color wheel to provide variance in our outputs. Ultimately, our model results in a personalized experience -- each user’s individual handwriting is translated to text and then results in a final visual output. Even if two users enter the same word, the visual output can vary due to the randomness in shape. Additionally, regardless of the probability of the text recognition, our model will always output some visual. This way, even if our text recognition is not highly accurate for a certain input, the user is still presented with a pleasing visual for an overall artistic experience.


## Discussion

Our final project is an interactive tool that allows a user to translate their own writing to an abstract visual form. A text recognition system "reads" the input and then the Python turtle library is used to generate a drawing based on the word that was predicted by the model. The written text influences the colors used to produce the drawing, but the patterns are generated randomly. Our initial intention was to closely replicate the experience of an individual with synesthesia, but through experimentation our team decided to take a more artistic approach to the concept of color-text association.

What makes this work unique is the translation from defined text to complete abstraction. Previous work such as the model created by Bock replicated synesthesia using a realistic approach, predicting a user's handwriting and coloring individual letters based on those predictions. Our approach is also systematic in the sense that a model is used to classify handwriting as accurately as possible, but the generative output cannot be predetermined as each user will see different results even with the same word input. Another distinction to note is our model for text recognition uses the entire word as an input, rather than individual letters.

Synesthesia is a unique phenomenon to study as it manifests itself in many different forms. We only looked at one type for this project, color-grapheme synesthesia, where an individual associates colors with text perception. Other types include chromesthesia (association between color and sound), spatial sequence synesthesia (numbers and spatial depth), and auditory-tactile synesthesia (sound and touch sensation). The experience of having these conditions could be replicated using a similar approach to our own in future work.

Our goal of this work was to explore the relationship between a real neurological condition and how it can be artificially reproduced using computational methods. The techniques studied could be applicable to scientific research in attempting to understand what these conditions are like for individuals who have them, as well as for creative use in generative art and music production.


(30 points, three to five paragraphs)

The first paragraph should be a short summary describing your results.

The subsequent paragraphs could address questions including:
- Why is this culturally innovative?
- How does your generative computational approach differ from traditional art/music/cultural production? 
- How do your results relate to broader social, cultural, economic political, etc., issues? 
- What are the ethical concerns for this form of generative art? 
- In what future directions could you expand this work?

## Team Roles

**Enrique**: Developed the widgets that are to be used by the user as well as its backend functionality. Handled various technical issues and enabled the tool to be used both locally and on Datahub. Connected the different components of the project to allow for a clean and user friendly tool.

## Technical Notes and Dependencies

**Platform**

The tool will run on both Datahub and locally. However, locally is recommended as the eventual visualization is both nicer and drawn faster. Datahub is unable to display a pop up window so the implementation of the drawing was different and restricted to the Mobilechelonian Python library which is a related but less powerful version of the Turtle library that can be used locally.

**Additional Libraries:** turtle, mobilechelonian, panel, holoviews, bokeh, socket, editdistance, opencv-python. In case run locally, a [requirements.txt](requirements.txt) file was included.

Any implementation details or notes we need to repeat your work. 
- Additional libraries you are using for this project
- Does this code require other pip packages, software, etc?
- Does this code need to run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

- https://www.researchgate.net/publication/323737970_A_Deep_Learning_Model_of_Perception_in_Color-Letter_Synesthesia
- https://towardsdatascience.com/synesthesia-an-inspiring-condition-for-ai-researchers-10cd57708855
- https://www.mdpi.com/2504-2289/2/1/8/pdf 
- https://synesthesia.me/see-your-name
- https://www.medicalnewstoday.com/articles/322807#Mechanisms-and-causes
- https://www.livescience.com/60707-what-is-synesthesia.html
- https://panel.holoviz.org/
- https://paulvanderlaken.com/2019/10/29/neural-synthesia-gan-ai-dreaming-of-music/
- https://designingsound.org/2017/12/20/mapping-sound-to-color/
- http://www.nicolasfournel.com/?page_id=125#comment-4827
- https://www.frontiersin.org/articles/10.3389/fnhum.2013.00603/full
- https://pdfs.semanticscholar.org/68d9/396eb744db2c586deec3d3fba250f7d33489.pdf
