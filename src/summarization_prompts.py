# summarization_prompts.py

"""
This file contains prompts used for clinical note summarization.
Modify these prompts to experiment with different summarization approaches.
"""

# Individual note summarization prompts
INDIVIDUAL_NOTE_PROMPTS = {
    "anthropic.claude": """
Please provide a concise medical summary of the following clinical note. 
Focus on key diagnostic findings, treatments, and recommendations:

{text}
""",
    
    "anthropic.claude-3-5": """
Please provide a concise medical summary of the following clinical note. 
Focus on key diagnostic findings, treatments, and recommendations:

{text}
""",
    
    "amazon.titan": """
Please provide a concise medical summary of the following clinical note. 
Focus on key diagnostic findings, treatments, and recommendations:

{text}
""",
    
    "meta.llama": """
Please provide a concise medical summary of the following clinical note. 
Focus on key diagnostic findings, treatments, and recommendations:

{text}
"""
}

# Chunk summarization prompts (for handling large sets of notes)
CHUNK_SUMMARIZATION_PROMPTS = {
    "anthropic.claude": """
I'm providing a subset of clinical notes for a patient or set of patients. Please create a summary of this information.

Focus on:
1. Key diagnostic findings in these notes
2. Important patterns or trends
3. Treatment approaches mentioned
4. Critical recommendations
5. Any notable patient information

Here are the clinical notes:

{text}
""",
    
    "anthropic.claude-3-5": """
I'm providing a subset of clinical notes for a patient or set of patients. Please create a summary of this information.

Focus on:
1. Key diagnostic findings in these notes
2. Important patterns or trends
3. Treatment approaches mentioned
4. Critical recommendations
5. Any notable patient information

Here are the clinical notes:

{text}
""",
    
    "amazon.titan": """
I'm providing a subset of clinical notes for a patient or set of patients. Please create a summary of this information.

Focus on:
1. Key diagnostic findings in these notes
2. Important patterns or trends
3. Treatment approaches mentioned
4. Critical recommendations
5. Any notable patient information

Here are the clinical notes:

{text}
""",
    
    "meta.llama": """
I'm providing a subset of clinical notes for a patient or set of patients. Please create a summary of this information.

Focus on:
1. Key diagnostic findings in these notes
2. Important patterns or trends
3. Treatment approaches mentioned
4. Critical recommendations
5. Any notable patient information

Here are the clinical notes:

{text}
"""
}

# Final summarization prompts (for combining chunk summaries)
FINAL_SUMMARIZATION_PROMPTS = {
    "anthropic.claude": """
I'm providing summaries of different sets of clinical notes. Please create a comprehensive summary that combines all this information.

Focus on:
1. Key diagnostic findings across all summaries
2. Important patterns or trends
3. Treatment approaches mentioned
4. Critical recommendations
5. Synthesize information to provide a coherent overview

Here are the chunk summaries:

{text}
""",
    
    "anthropic.claude-3-5": """
I'm providing summaries of different sets of clinical notes. Please create a comprehensive summary that combines all this information.

Focus on:
1. Key diagnostic findings across all summaries
2. Important patterns or trends
3. Treatment approaches mentioned
4. Critical recommendations
5. Synthesize information to provide a coherent overview

Here are the chunk summaries:

{text}
""",
    
    "amazon.titan": """
I'm providing summaries of different sets of clinical notes. Please create a comprehensive summary that combines all this information.

Focus on:
1. Key diagnostic findings across all summaries
2. Important patterns or trends
3. Treatment approaches mentioned
4. Critical recommendations
5. Synthesize information to provide a coherent overview

Here are the chunk summaries:

{text}
""",
    
    "meta.llama": """
I'm providing summaries of different sets of clinical notes. Please create a comprehensive summary that combines all this information.

Focus on:
1. Key diagnostic findings across all summaries
2. Important patterns or trends
3. Treatment approaches mentioned
4. Critical recommendations
5. Synthesize information to provide a coherent overview

Here are the chunk summaries:

{text}
"""
}

# Combined note summarization prompts (for full set of notes)
COMBINED_NOTE_PROMPTS = {
    "anthropic.claude": """
You are provided with a combined clinical note file that merges all original clinical documentation for a patient. Your task is to synthesize all this information into a comprehensive clinical progress note, following the standardized format below. Ensure that every relevant detail is captured accurately under the correct section and that the final note is written in a clear, organized, and professional narrative. Do not include any bibliographic references.

Please structure the progress note with the following sections and headings:

1. Patient & Encounter Information:
   - Include the patient's name/ID, date of birth, age, gender, appointment date/time, and any referring provider or additional encounter details.

2. Reason for Consultation and History of Present Illness:
   - Summarize the chief complaint or reason for the consultation and provide a detailed narrative of the history of present illness including onset, progression, and pertinent events.

3. Past History:
   - Provide information on past medical history, surgical history, pregnancy/birth/developmental history (if applicable), family history, and social history.

4. Review of Systems:
   - List the relevant positives and negatives for each body system (e.g., HEENT, cardiovascular, pulmonary, gastrointestinal, neurological, dermatological, etc.).

5. Previous Testing and Imaging:
   - Summarize key findings from laboratory tests, imaging studies, genetic tests, and other diagnostic evaluations.

6. Physical Examination:
   - Document the physical exam findings in a head-to-toe format, including any quantifiable measurements and notable observations.

7. Genomic/Genetic Information (if applicable):
   - Include any pertinent genomic interpretation details and summarize the genetic counselor's assessments or recommendations.

8. Physician Assessment and Plan:
   - Provide a focused clinical assessment that integrates all the findings, including differential diagnoses if applicable, and clearly outline the management plan, further testing, referrals, and follow-up instructions.

9. Time and Coordination Summary:
   - Specify the total time spent during the encounter, detailing time for review, examination, counseling, documentation, and coordination.

Here are the combined clinical notes, each separated by file identifiers:

{text}
""",
    
    "anthropic.claude-3-5": """
You are provided with a combined clinical note file that merges all original clinical documentation for a patient. Your task is to synthesize all this information into a comprehensive clinical progress note, following the standardized format below. Ensure that every relevant detail is captured accurately under the correct section and that the final note is written in a clear, organized, and professional narrative. Do not include any bibliographic references.

Please structure the progress note with the following sections and headings:

1. Patient & Encounter Information:
   - Include the patient's name/ID, date of birth, age, gender, appointment date/time, and any referring provider or additional encounter details.

2. Reason for Consultation and History of Present Illness:
   - Summarize the chief complaint or reason for the consultation and provide a detailed narrative of the history of present illness including onset, progression, and pertinent events.

3. Past History:
   - Provide information on past medical history, surgical history, pregnancy/birth/developmental history (if applicable), family history, and social history.

4. Review of Systems:
   - List the relevant positives and negatives for each body system (e.g., HEENT, cardiovascular, pulmonary, gastrointestinal, neurological, dermatological, etc.).

5. Previous Testing and Imaging:
   - Summarize key findings from laboratory tests, imaging studies, genetic tests, and other diagnostic evaluations.

6. Physical Examination:
   - Document the physical exam findings in a head-to-toe format, including any quantifiable measurements and notable observations.

7. Genomic/Genetic Information (if applicable):
   - Include any pertinent genomic interpretation details and summarize the genetic counselor's assessments or recommendations.

8. Physician Assessment and Plan:
   - Provide a focused clinical assessment that integrates all the findings, including differential diagnoses if applicable, and clearly outline the management plan, further testing, referrals, and follow-up instructions.

9. Time and Coordination Summary:
   - Specify the total time spent during the encounter, detailing time for review, examination, counseling, documentation, and coordination.

Here are the combined clinical notes, each separated by file identifiers:

{text}
""",
    
    "amazon.titan": """
You are provided with a combined clinical note file that merges all original clinical documentation for a patient. Your task is to synthesize all this information into a comprehensive clinical progress note, following the standardized format below. Ensure that every relevant detail is captured accurately under the correct section and that the final note is written in a clear, organized, and professional narrative. Do not include any bibliographic references.

Please structure the progress note with the following sections and headings:

1. Patient & Encounter Information:
   - Include the patient's name/ID, date of birth, age, gender, appointment date/time, and any referring provider or additional encounter details.

2. Reason for Consultation and History of Present Illness:
   - Summarize the chief complaint or reason for the consultation and provide a detailed narrative of the history of present illness including onset, progression, and pertinent events.

3. Past History:
   - Provide information on past medical history, surgical history, pregnancy/birth/developmental history (if applicable), family history, and social history.

4. Review of Systems:
   - List the relevant positives and negatives for each body system (e.g., HEENT, cardiovascular, pulmonary, gastrointestinal, neurological, dermatological, etc.).

5. Previous Testing and Imaging:
   - Summarize key findings from laboratory tests, imaging studies, genetic tests, and other diagnostic evaluations.

6. Physical Examination:
   - Document the physical exam findings in a head-to-toe format, including any quantifiable measurements and notable observations.

7. Genomic/Genetic Information (if applicable):
   - Include any pertinent genomic interpretation details and summarize the genetic counselor's assessments or recommendations.

8. Physician Assessment and Plan:
   - Provide a focused clinical assessment that integrates all the findings, including differential diagnoses if applicable, and clearly outline the management plan, further testing, referrals, and follow-up instructions.

9. Time and Coordination Summary:
   - Specify the total time spent during the encounter, detailing time for review, examination, counseling, documentation, and coordination.

Here are the combined clinical notes, each separated by file identifiers:

{text}
""",
    
    "meta.llama": """
You are provided with a combined clinical note file that merges all original clinical documentation for a patient. Your task is to synthesize all of this information into one comprehensive clinical progress note according to the standardized format described below. Make sure all relevant details are accurately organized into the appropriate sections and that the final note is presented in a clear, coherent, and professional manner. Do not include any bibliographic references.

Please include the following sections with clear headings:

1. Patient & Encounter Information:
   - Patient name/ID, date of birth, age, gender, appointment date/time, and any referring provider information.

2. Reason for Consultation and History of Present Illness:
   - A summary of the chief complaint/reason for consultation and a detailed narrative of the history of present illness including onset, progression, and relevant events.

3. Past History:
   - Include past medical history, surgical history, pregnancy/birth/developmental history (when applicable), family history, and social history.

4. Review of Systems:
   - Provide a system-by-system review highlighting significant positives and negatives (e.g., HEENT, cardiovascular, pulmonary, gastrointestinal, neurological, dermatological, etc.).

5. Previous Testing and Imaging:
   - Summarize important findings from laboratory evaluations, imaging studies, genetic tests, and other diagnostics.

6. Physical Examination:
   - Record the physical examination findings in a structured head-to-toe format, including any measurements or notable clinical observations.

7. Genomic/Genetic Information (if applicable):
   - Document key features relevant to genomic interpretation and include any genetic counseling assessments or recommendations.

8. Physician Assessment and Plan:
   - Provide a clinically focused assessment that synthesizes the collected information and outlines a management plan, including any recommended testing, referrals, or treatments.

9. Time and Coordination Summary:
   - Include the total time spent on the encounter, detailing activities such as reviewing, examining, counseling, documentation, and care coordination.

Below are the combined clinical notes, each separated by file identifiers:

{text}
"""
}

# Question-answering prompts for chat interface
QA_PROMPTS = {
    "anthropic.claude": """
I'm going to provide you with clinical notes. Then I will ask you questions. 
When answering my questions:
1. ONLY use information found in these clinical notes
2. If the answer cannot be determined from the notes, say "I don't have enough information to answer that question based on the clinical notes provided."
3. DO NOT make up or infer information that is not explicitly stated in the notes
4. Cite specific files when appropriate

Here are the clinical notes:

{context}

My question is: {query}
""",
    
    "anthropic.claude-3-5": """
I'm going to provide you with clinical notes. Then I will ask you questions. 
When answering my questions:
1. ONLY use information found in these clinical notes
2. If the answer cannot be determined from the notes, say "I don't have enough information to answer that question based on the clinical notes provided."
3. DO NOT make up or infer information that is not explicitly stated in the notes
4. Cite specific files when appropriate

Here are the clinical notes:

{context}

My question is: {query}
""",
    
    "amazon.titan": """
I'm going to provide you with clinical notes. Then I will ask you questions. 
When answering my questions:
1. ONLY use information found in these clinical notes
2. If the answer cannot be determined from the notes, say "I don't have enough information to answer that question based on the clinical notes provided."
3. DO NOT make up or infer information that is not explicitly stated in the notes
4. Cite specific files when appropriate

Here are the clinical notes:

{context}

My question is: {query}
""",
    
    "meta.llama": """
I'm going to provide you with clinical notes. Then I will ask you questions. 
When answering my questions:
1. ONLY use information found in these clinical notes
2. If the answer cannot be determined from the notes, say "I don't have enough information to answer that question based on the clinical notes provided."
3. DO NOT make up or infer information that is not explicitly stated in the notes
4. Cite specific files when appropriate

Here are the clinical notes:

{context}

My question is: {query}
"""
}