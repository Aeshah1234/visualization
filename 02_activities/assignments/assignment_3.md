# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 

VISUAL ONE: DISTRIBUTION OF MENTAL HEALTH SERVICES ACROSS FORMER TORONTO MUNICIPALITIES

    > What software did you use to create your data visualization?
    Python with the incorporation of the matplotlib library. 

    > Who is your intended audience? 
    Because it is a city-based data, I made the assumption that my audience would be diverse. It could include people in the government, mental health professionals, and general public. 

    > What information or message are you trying to convey with your visualization? 
    The visualization communicat4es the uneven geographic distribution of mental health services across Toronto's six former municipalities. The bar chart makes immediately visible that there is a disproportionate service allocation. For example, compared to former Toronto, York and Etobicoke are underserviced relative to their geographic size and population. The main message is that where one lives has an influence on proximity to mental health support and service utilization. 
    
    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
    Because the anticipated audience was assumed to be diverse, I focused on the following points: 
        1. Clarity and simplicity: a horizontal bar chart was chosen because it showed clearly municipality names and associated figure without overlap or clutter 
        2. Labeling: appropriate labels and neutral title were selected to advance the intended message without misleading the reader or providing author's bias
        3. Font style: Different font sizes were used to indicate titles and labels, but were increased to provide clarity. Color was consistent to suggest a level of formality intended for the purpose of the visual and topic
        4. Color: one color for the bars (a blue color close to the colors of the city of Toronto) was used to reflect that it's a city-affiliated report. In addition to the white background and black for titles and labels, the palette is considered reserved and formal, which I thought is necessary for the topic and audience in mind
        5. Source: added the source of the dataset for transparency and credibility purposes
    
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    Reproducibility was ensured by producing the visualization through a Python script that includes useful comments that help an individual run the code, given that they have the dataset file. I also added a code to produce the visual with a fixed resolution (150 dpi), ensuring that the visual is consistent across runs. 
    
    > How did you ensure that your data visualization is accessible?  
    The aspects of design discussed above were strategically considered to ensure that the visualization is accessible to a diverse group of people. Color palette is simple and formal, maintaining a strong contrast against a white background. Because only one color is used, there is no risk of confusing the categories. Text size and color are carefully used to aslo address accessible design, with numerical values appearing directly on teh chart rather than requiring the reader to trace bars to a scale. 
    
    > Who are the individuals and communities who might be impacted by your visualization?  
    There are several groups who might be impacted by this visual including: 
            1. General public: residents of these areas who rely on local mental health services, as it can inform their decisions for advocacy and service utilization. This can be especially useful for racialized, low-income, and newcomer communities
            2. Mental health service provides: the visual can inform decisions surrounding inadequate services and allocation needs 
            3. Policy makers / government: decision-makers who see this chart may use it to justify or advocate for funding allocations and service expansion plans 
    
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    I was intentional in how I wanted to use the dataset to convey and important and simple message about mental services. Therefore based on the dataset and out of the 25 columns included, I focused on municipality and number of services. There were other useful variables such as neighbourhood and legal status. But I excluded neighbourhood for example because it would have produced an unreadable chart given its close to 100 unique values. I would have picked it if I were to design an interactive map of one specific municipality. 
    
    > What ‘underwater labour’ contributed to your final data visualization product?
    The most important labour was the time spent to explore the dataset and make decisions what messages I wanted to get across and for what audiences/purposes. Because of my proximity to the mental health services and knowledge of service shortage, I wanted to see how that data would look like mapped out (even though it is relatively dated and 'retired' by the city). 

VISUAL TWO: MENTAL HEALTH SERVICES ACCESSIBLITY ACROSS FORMER TORONTO 
> What software did you use to create your data visualization?
    I used Python to clean the data and Excel to graph it. 
    
> Who is your intended audience?  
    Same as visual one, but with a special focus on people with disability needs and advocate groups/organizations. 
    
> What information or message are you trying to convey with your visualization? 
    The visual conveys the extent to which mental health services organizations across Toronto's former municipalities are physically accessible to people with mobility challenges/needs. 

> What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
  1. Chart type: I opted for another simple and clear chart to ensure that it's widely readable and accessible among different audiences
  2. Color choice: I chose three colors to indicate the the status of accessiblity. The color blue which represents the city seemed to be an appropriate choice to indicate the presence of accesibility, while red was strong enough of a color to suggest the absence of such important element and yellow to suggest ambivalence and need to investigate further
  3. Font size and color: I kept the font type and size standard, but still readable and clear. The color combination of black for titles and labels and while for figures seemed also appropriate and consistent. 
  4. Source: I added the source for credibility and transparency. 
  Overall, I attempted to created a visual that is clear and effective, but also matched the asethetics of the pervious visual to communicate a formal report associated with the city. 



- This assignment is intentionally open-ended - you are free to create static or dynamic data visualizations, maps, or whatever form of data visualization you think best communicates your information to your audience of choice! 
- Total word count should not exceed **(as a maximum) 1000 words** 
 
### Why am I doing this assignment?:  
- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes: 
* Create and customize data visualizations from start to finish in Python
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story  
- This would be a great project to include in your GitHub Portfolio – put in the effort to make it something worthy of showing prospective employers!

### Rubric:

| Component         | Scoring  | Requirement                                                                 |
|-------------------|----------|-----------------------------------------------------------------------------|
| Data Visualizations | Complete/Incomplete | - Data visualizations are distinct from each other<br>- Data visualizations are clearly identified<br>- Different sources/rationales (text with two images of data, if visualizations are labeled)<br>- High-quality visuals (high resolution and clear data)<br>- Data visualizations follow best practices of accessibility |
| Written Explanations | Complete/Incomplete | - All questions from assignment description are answered for each visualization<br>- Explanations are supported by course content or scholarly sources, where needed |
| Code              | Complete/Incomplete | - All code is included as an appendix with your final submissions<br>- Code is clearly commented and reproducible |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 -  2026-06-16`
* The branch name for your repo should be: `assignment-3`
* What to submit for this assignment:
    * A folder/directory containing:
        * Two distinct data visualizations (for example, PNGs, PDFs, or screenshots)
        * Two Markdown files answering all questions for each visualization (including a link to your dataset in both files)
        * One Python file contains the complete code and visualization, and another file (with or without code) contains the visualization.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-3`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
