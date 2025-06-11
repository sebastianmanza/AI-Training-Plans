import { useState } from 'react'
import Question from './Question'
import { questions } from '../data/usersurveyquestions'

export default function UserSurvey({ onComplete }) {
    const [index, setIndex] = useState(0)
    const [answers, setAnswers] = useState({})
  
    const current = questions[index]
  
    function handleAnswer(value) {
      setAnswers(a => ({ ...a, [current.id]: value }))
    }
  
    function next() {
      if (index < questions.length - 1) {
        setIndex(i => i + 1)
      } else {
        onComplete(answers)
      }
    }
  
    function back() {
      if (index > 0) setIndex(i => i - 1)
    }
  
    return (
      <div>
        <Question
          data={current}
          value={answers[current.id]}
          onChange={handleAnswer}
        />
        <div style={{ marginTop: '1rem' }}>
          <button onClick={back} disabled={index === 0}>
            Back
          </button>
          <button onClick={next}>
            {index < questions.length - 1 ? 'Next' : 'Submit'}
          </button>
        </div>
      </div>
    )
  }