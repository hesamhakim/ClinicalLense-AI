# healthcare_provider_questions.py

"""
This module contains predefined questions organized by healthcare provider profiles and question sets.
Each profile represents a healthcare professional with a title in the format "Name (Title)".
At this stage, all profiles share the same five question sets, which can be customized later.
"""

QUESTION_LIBRARY = {
    "Sam (Genetic Counselor II)": {
        "Medical History": [
            "What is the patient's primary diagnosis?",
            "When was the patient first diagnosed with their condition?",
            "What previous treatments has the patient received?",
            "Does the patient have any chronic conditions?",
            "What surgeries has the patient undergone in the past?",
            "Are there any notable hospitalizations in the patient's history?"
        ],
        "Genetic": [
            "What genetic tests have been performed?",
            "Are there any known genetic mutations or variants?",
            "What is the inheritance pattern related to this condition?",
            "How might genetic factors influence the treatment plan?",
            "Were any follow-up genetic tests recommended?",
            "What genetic counseling was provided to the patient?"
        ],
        "Family History": [
            "Is there any family history of genetic disorders?",
            "Have any relatives undergone genetic testing?",
            "What hereditary conditions are present in the family?",
            "How has family history influenced diagnostic decisions?",
            "Were family members advised to pursue testing?",
            "How do familial trends impact patient management?"
        ],
        "Risk Assessment": [
            "What risk factors are identified in the clinical notes?",
            "How does the patient's genetic profile affect risk analysis?",
            "Are there any environmental or lifestyle risks mentioned?",
            "What preventive measures were discussed?",
            "How is the overall risk profile affecting treatment options?",
            "What additional risk assessments are recommended?"
        ],
        "Counseling Approach": [
            "What counseling strategies were employed during the session?",
            "How was patient education addressed?",
            "Were any decision aids used to facilitate understanding?",
            "How did the counselor address patient concerns?",
            "What follow-up counseling recommendations were made?",
            "How was the patient’s informed consent documented?"
        ]
    },
    "Alex (Genetic Counselor III)": {
        "Medical History": [
            "What is the patient's primary diagnosis?",
            "When was the patient first diagnosed with their condition?",
            "What previous treatments has the patient received?",
            "Does the patient have any chronic conditions?",
            "What surgeries has the patient undergone in the past?",
            "Are there any notable hospitalizations in the patient's history?"
        ],
        "Genetic": [
            "What genetic tests have been performed?",
            "Are there any known genetic mutations or variants?",
            "What is the inheritance pattern related to this condition?",
            "How might genetic factors influence the treatment plan?",
            "Were any follow-up genetic tests recommended?",
            "What genetic counseling was provided to the patient?"
        ],
        "Family History": [
            "Is there any family history of genetic disorders?",
            "Have any relatives undergone genetic testing?",
            "What hereditary conditions are present in the family?",
            "How has family history influenced diagnostic decisions?",
            "Were family members advised to pursue testing?",
            "How do familial trends impact patient management?"
        ],
        "Risk Assessment": [
            "What risk factors are identified in the clinical notes?",
            "How does the patient's genetic profile affect risk analysis?",
            "Are there any environmental or lifestyle risks mentioned?",
            "What preventive measures were discussed?",
            "How is the overall risk profile affecting treatment options?",
            "What additional risk assessments are recommended?"
        ],
        "Counseling Approach": [
            "What counseling strategies were employed during the session?",
            "How was patient education addressed?",
            "Were any decision aids used to facilitate understanding?",
            "How did the counselor address patient concerns?",
            "What follow-up counseling recommendations were made?",
            "How was the patient’s informed consent documented?"
        ]
    },
    "Lisa (Genetic Counselor I)": {
        "Medical History": [
            "What is the patient's primary diagnosis?",
            "When was the patient first diagnosed with their condition?",
            "What previous treatments has the patient received?",
            "Does the patient have any chronic conditions?",
            "What surgeries has the patient undergone in the past?",
            "Are there any notable hospitalizations in the patient's history?"
        ],
        "Genetic": [
            "What genetic tests have been performed?",
            "Are there any known genetic mutations or variants?",
            "What is the inheritance pattern related to this condition?",
            "How might genetic factors influence the treatment plan?",
            "Were any follow-up genetic tests recommended?",
            "What genetic counseling was provided to the patient?"
        ],
        "Family History": [
            "Is there any family history of genetic disorders?",
            "Have any relatives undergone genetic testing?",
            "What hereditary conditions are present in the family?",
            "How has family history influenced diagnostic decisions?",
            "Were family members advised to pursue testing?",
            "How do familial trends impact patient management?"
        ],
        "Risk Assessment": [
            "What risk factors are identified in the clinical notes?",
            "How does the patient's genetic profile affect risk analysis?",
            "Are there any environmental or lifestyle risks mentioned?",
            "What preventive measures were discussed?",
            "How is the overall risk profile affecting treatment options?",
            "What additional risk assessments are recommended?"
        ],
        "Counseling Approach": [
            "What counseling strategies were employed during the session?",
            "How was patient education addressed?",
            "Were any decision aids used to facilitate understanding?",
            "How did the counselor address patient concerns?",
            "What follow-up counseling recommendations were made?",
            "How was the patient’s informed consent documented?"
        ]
    }
}


def get_provider_profiles():
    """
    Return a list of all healthcare provider profiles.
    """
    return list(QUESTION_LIBRARY.keys())


def get_question_sets(provider_name):
    """
    Given a provider's name, return the corresponding dictionary of question sets.
    If the provider is not found, return an empty dictionary.
    """
    return QUESTION_LIBRARY.get(provider_name, {})


if __name__ == "__main__":
    # Example usage: Print the questions for each provider profile.
    for provider, question_sets in QUESTION_LIBRARY.items():
        print(f"\nProvider: {provider}")
        for set_name, questions in question_sets.items():
            print(f"  {set_name}:")
            for question in questions:
                print(f"    - {question}")