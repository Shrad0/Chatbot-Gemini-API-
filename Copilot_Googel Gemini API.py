#!/usr/bin/env python
# coding: utf-8

# In[1]:


import google.generativeai as genai


# In[2]:


# Set up Google Gemini API Key
genai.configure(api_key="...")  # Replace with your actual API key


# In[3]:


# Function to generate a test from a job description
def generate_test(job_description):
    prompt = f"""
    You are an AI assistant helping HR create job assessments.
    Given the following job description:
    {job_description}

    1️⃣ Extract key job roles and required skills.
    2️⃣ Suggest test sections (e.g., Aptitude, Coding, Technical, HR).
    3️⃣ Generate **5 relevant sample questions** for each section.
    4️⃣ Provide multiple-choice options (where applicable) and correct answers.

    Structure the output **clearly and concisely**.
    """

    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Using the best model
    response = model.generate_content(prompt)
    return response.text


# In[4]:


# Example Job Description
job_description = """
We are looking for a Python Developer with expertise in Django, REST APIs, and SQL databases. 
The candidate should have strong problem-solving skills and experience with data structures and algorithms.
"""


# In[5]:


# Run the function and print results
test_output = generate_test(job_description)
print("\n--- AI-Generated Test Suggestions ---\n")
print(test_output)


# In[6]:


# Example Job Description
job_description = """
We are looking for a Full-Stack Developer with experience in React.js, Node.js, and MongoDB. The ideal candidate should have a strong understanding of front-end and back-end technologies and be able to build scalable web applications.
"""


# In[7]:


# Run the function and print results
test_output = generate_test(job_description)
print("\n--- AI-Generated Test Suggestions ---\n")
print(test_output)


# In[9]:


# Example Job Description
job_description = """
We are hiring an AI/ML Engineer to develop machine learning models for real-world applications. The candidate should be proficient in Python, TensorFlow/PyTorch, and cloud-based AI services.
"""
# Run the function and print results
test_output = generate_test(job_description)
print("\n--- AI-Generated Test Suggestions ---\n")
print(test_output)


# In[10]:


# Example Job Description
job_description = """
We are looking for a DevOps Engineer to automate infrastructure and improve CI/CD workflows. Experience in AWS, Kubernetes, Terraform, and Jenkins is required.
"""
# Run the function and print results
test_output = generate_test(job_description)
print("\n--- AI-Generated Test Suggestions ---\n")
print(test_output)

