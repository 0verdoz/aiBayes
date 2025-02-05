from flask import Flask, request, render_template, jsonify, json
from inference import MoodStressFact, MoodStressEngine

app = Flask(__name__)
questions = {
    1: "In the last month, how often have you been upset because of something that happened unexpectedly?",
    2: "In the last month, how often have you felt that you were unable to control the important things in your life?",
    3: "In the last month, how often have you felt nervous and stressed?",
    4: "In the last month, how often have you felt confident about your ability to handle your personal problems?",
    5: "In the last month, how often have you felt that things were going your way?",
    6: "In the last month, how often have you found that you could not cope with all the things that you had to do?",
    7: "In the last month, how often have you been able to control irritations in your life?",
    8: "In the last month, how often have you felt that you were on top of things?",
    9: "In the last month, how often have you been angered because of things that happened that were outside of your control?",
    10: "In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?"
}


@app.route('/', methods=['GET', 'POST'])
def mood_stress():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        
        # Run the engine
        engine = MoodStressEngine()
        engine.reset()
        engine.declare(MoodStressFact(**data))
        engine.run()

        # Collect Results
        results = {fact.get('stress', 'Unknown Stress'): fact.get('mood_state', 'Unknown Mood') for fact in engine.facts.values() if 'stress' in fact}
        print(engine.facts.values())
        return jsonify(results)

    return render_template('form.html', questions=questions)

@app.route('/results')
def results():
    data = request.args.get('data')
    if data:
        try:
            parsed_data = json.loads(data)
            print(parsed_data)
            return render_template('results.html', results=parsed_data)  # Pass to template
        except json.JSONDecodeError:
            return render_template('form.html', questions=questions)
    return render_template('form.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)