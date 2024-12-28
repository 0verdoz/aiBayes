# Psychology Expert System

A web-based expert system that helps identify stress levels and provides recommendations based on user interactions. The system combines a React frontend for user interaction with a Prolog backend for expert knowledge processing.

## Project Structure

```
psych-expert-system/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # React components
│   │   │   ├── Chat/
│   │   │   │   ├── ChatInterface.jsx
│   │   │   │   ├── MessageList.jsx
│   │   │   │   └── UserInput.jsx
│   │   │   ├── Form/
│   │   │   │   ├── AssessmentForm.jsx
│   │   │   │   └── FormFields.jsx
│   │   │   └── common/
│   │   │       ├── Header.jsx
│   │   │       └── LoadingSpinner.jsx
│   │   ├── services/
│   │   │   └── api.js      # API integration with Prolog backend
│   │   ├── utils/
│   │   │   └── helpers.js  # Utility functions
│   │   ├── App.jsx
│   │   └── index.jsx
│   └── package.json
│
├── backend/                  # Prolog backend
│   ├── src/
│   │   ├── server.pl        # Main server file
│   │   ├── knowledge_base/
│   │   │   ├── symptoms.pl  # Stress symptoms and indicators
│   │   │   ├── rules.pl     # Expert system rules
│   │   │   └── advice.pl    # Recommendations and next steps
│   │   └── utils/
│   │       └── helpers.pl   # Helper predicates
│   └── tests/
│       └── test_rules.pl
│
└── README.md
```

## Technology Stack

- Frontend: React 18+
- Backend: SWI-Prolog with Pengines for web integration
- API Communication: REST API using HTTP
- Styling: Tailwind CSS
- Testing: Jest (Frontend), PLUnit (Prolog)

## Core Features

1. Chat-based interface for natural interaction
2. Optional structured form input for detailed assessments
3. Real-time stress level evaluation
4. Personalized recommendations
5. Session history tracking

## Getting Started

### Prerequisites

- Node.js 16+
- SWI-Prolog 8+
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-org/psych-expert-system.git
cd psych-expert-system
```

2. Set up the frontend:
```bash
cd frontend
npm install
```

3. Set up the Prolog backend:
```bash
cd backend
swipl src/server.pl
```

## Knowledge Base Structure

The Prolog knowledge base is organized into three main components:

1. **Symptoms (symptoms.pl)**
   - Stress indicators
   - Severity levels
   - Physical and psychological manifestations

2. **Rules (rules.pl)**
   - Inference rules for stress evaluation
   - Pattern matching for user inputs
   - Decision trees for recommendations

3. **Advice (advice.pl)**
   - Recommendation database
   - Coping strategies
   - Professional referral criteria

## API Endpoints

- `POST /api/analyze`: Submit user message for analysis
- `POST /api/assess`: Submit form data for assessment
- `GET /api/recommendations`: Get personalized recommendations
- `GET /api/history`: Retrieve session history

## Extending the System

### Adding New Rules

To add new psychological rules to the system, modify `backend/src/knowledge_base/rules.pl`:

```prolog
% Example rule structure
stress_level(high) :-
    has_symptom(sleep_issues),
    has_symptom(anxiety),
    symptom_duration(Days),
    Days > 14.
```

### Adding New UI Components

Create new React components in `frontend/src/components/` following the existing pattern:

```jsx
// Example new component
const StressChart = ({ data }) => {
  // Component implementation
};
```

## Development Guidelines

1. **Knowledge Base Updates**
   - Keep rules atomic and modular
   - Document all predicates
   - Add test cases for new rules

2. **Frontend Development**
   - Use functional components
   - Implement error boundaries
   - Follow React best practices

3. **Testing**
   - Write unit tests for all new rules
   - Test edge cases in user inputs
   - Validate recommendation logic

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Submit pull request

## License

MIT License

## Support

For support or questions, please open an issue in the repository.
