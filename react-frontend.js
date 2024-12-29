// ChatInterface.jsx
import React, { useState, useEffect } from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';
import { analyzeMessage } from '../../services/api';

const ChatInterface = () => {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSendMessage = async (message) => {
    setLoading(true);
    setMessages(prev => [...prev, { type: 'user', content: message }]);
    
    try {
      const response = await analyzeMessage(message);
      setMessages(prev => [...prev, {
        type: 'system',
        content: response.recommendations.join('\n'),
        stressLevel: response.stress_level
      }]);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full">
      <MessageList messages={messages} />
      <UserInput onSend={handleSendMessage} disabled={loading} />
    </div>
  );
};

// AssessmentForm.jsx
import React, { useState } from 'react';
import FormFields from './FormFields';
import { submitAssessment } from '../../services/api';

const AssessmentForm = () => {
  const [formData, setFormData] = useState({
    sleep: 0,
    anxiety: 0,
    concentration: 0,
    fatigue: 0,
    irritability: 0
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await submitAssessment(formData);
      // Handle response
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <FormFields formData={formData} setFormData={setFormData} />
      <button type="submit" className="btn-primary">
        Submit Assessment
      </button>
    </form>
  );
};

// api.js
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:3000/api';

export const analyzeMessage = async (message) => {
  const response = await fetch(`${API_BASE_URL}/analyze`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message }),
  });
  return response.json();
};

export const submitAssessment = async (formData) => {
  const response = await fetch(`${API_BASE_URL}/assess`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(formData),
  });
  return response.json();
};

// App.jsx
import React, { useState } from 'react';
import ChatInterface from './components/Chat/ChatInterface';
import AssessmentForm from './components/Form/AssessmentForm';

const App = () => {
  const [view, setView] = useState('chat');

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow-sm">
        <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex">
              <button
                onClick={() => setView('chat')}
                className={`px-3 py-2 rounded-md ${
                  view === 'chat' ? 'bg-gray-900 text-white' : 'text-gray-300'
                }`}
              >
                Chat
              </button>
              <button
                onClick={() => setView('form')}
                className={`px-3 py-2 rounded-md ${
                  view === 'form' ? 'bg-gray-900 text-white' : 'text-gray-300'
                }`}
              >
                Assessment Form
              </button>
            </div>
          </div>
        </nav>
      </header>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        {view === 'chat' ? <ChatInterface /> : <AssessmentForm />}
      </main>
    </div>
  );
};

export default App;
