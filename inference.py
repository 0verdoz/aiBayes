from experta import *

# Define Facts
from experta import *

class MoodStressFact(Fact):
    """Defines the structure of inputs"""
    mood = Field(str)
    sleep = Field(int)
    activity = Field(int)
    major_event = Field(bool)
    q1 = Field(str)
    q2 = Field(str)
    q3 = Field(str)
    q4 = Field(str)
    q5 = Field(str)
    q6 = Field(str)
    q7 = Field(str)
    q8 = Field(str)
    q9 = Field(str)
    q10 = Field(str)

class MoodStressEngine(KnowledgeEngine):

    @Rule(MoodStressFact(mood="sad", sleep=P(lambda x: x < 4)))
    def high_stress_low_mood(self):
        self.declare(Fact(stress="High", mood_state="Low"))

    @Rule(MoodStressFact(mood="happy", sleep=P(lambda x: x > 6)))
    def low_stress_happy(self):
        self.declare(Fact(stress="Low", mood_state="Happy"))

    @Rule(MoodStressFact(mood="anxious", major_event=True))
    def high_stress_anxious(self):
        self.declare(Fact(stress="High", mood_state="Anxious"))

    # PSS-based rules
    @Rule(
        AS.fact << MoodStressFact(
            q1=MATCH.q1, q2=MATCH.q2, q3=MATCH.q3, q4=MATCH.q4, q5=MATCH.q5,
            q6=MATCH.q6, q7=MATCH.q7, q8=MATCH.q8, q9=MATCH.q9, q10=MATCH.q10
        )
    )
    def calculate_pss_score(self, fact, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        """Calculate stress level based on PSS test responses"""

        # Convert Likert scale answers to numeric scores
        score_mapping = {
            "never": 0,
            "almost never": 1,
            "sometimes": 2,
            "fairly often": 3,
            "very often": 4
        }

        # Convert responses into numerical scores
        scores = [score_mapping.get(q, 0) for q in [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]]

        # PSS calculation (inverted scoring for q4, q5, q7, q8)
        total_pss_score = sum(scores) - (2 * (score_mapping.get(q4, 0) + score_mapping.get(q5, 0) +
                                              score_mapping.get(q7, 0) + score_mapping.get(q8, 0)))

        # Determine stress level based on PSS score
        if total_pss_score <= 13:
            stress_level = "Low"
        elif 14 <= total_pss_score <= 26:
            stress_level = "Moderate"
        else:
            stress_level = "High"

        self.declare(Fact(stress=stress_level, pss_score=total_pss_score, ))

        print(f"Calculated PSS Score: {total_pss_score}, Stress Level: {stress_level}")


def main():# Collect Inputs
    mood_input = input("How do you feel (e.g., happy, sad, anxious, anger, joy)? ").strip().lower()
    sleep_input = int(input("How many hours did you sleep last night? "))
    activity_input = int(input("How many minutes did you exercise today? "))
    major_event_input = input("Did you have a major event today (yes/no)? ").strip().lower() == "yes"

    # Initialize and Run the Engine
    engine = MoodStressEngine()
    engine.reset()
    engine.declare(MoodStressFact(mood=mood_input, sleep=sleep_input, activity=activity_input, major_event=major_event_input))
    engine.run()

    # Print Results
    for fact in engine.facts.values():
        if fact.get("stress"):
            print(f"Stress Level: {fact['stress']}")
        if fact.get("mood_state"):
            print(f"Mood: {fact['mood_state']}")

if __name__ == "__main__":
    main()