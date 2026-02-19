class LLMRefinement:

    def refine_intent(self, query, ml_intent):
        prompt = f"""
        Student Query: "{query}"
        ML Predicted Intent: {ml_intent}

        Verify whether the intent is correct among:
        [Explanation, Example, Doubt clarification, Revision]

        Return the final intent label only.
        """

        # Simulated refinement (replace with real LLM API in production)
        return ml_intent
