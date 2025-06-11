export const questions = [
    { id: 1, text: 'Date of Birth:', type: 'date' },
    { id: 2, text: 'Sex:', type: 'select',
      options: ['Male','Female','Enter:'] },
    { id: 3, text: 'Running Experience:', type: 'select',
      options: ['Advanced', 'Intermediate', 'Beginner'] },
    { id: 4, text: 'How many days would you like to run? (At most 2 more days than you currently run):', type: 'select',
      options: [2, 3, 4, 5, 6, 7] },
    { id: 5, text: 'What days of the week can you commit at least an hour for a run?:', type: 'select',
      options: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] },
    { id: 6, text: 'What day do you have the most time for a run?', type: 'select',
      options: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] },
    { id: 7, text: 'Current estimated 5k fitness? (how fast can you run a 5k or 3.1 miles in mm:ss)', type: 'time' },
    { id: 8, text: 'How many major injuries have you had in the past 2 years? (injuries that prevented you from running for more than two weeks)', type: 'slider',
      options: [0, 1, 2, 3, 4, 5, 6] }, 
    { id: 9, text: 'How long ago was your most recent injury?', type: 'select',
      options: ['< 2 months', '2 - 4 months', '4 - 8 months', '8 months - 2 years', 'NA'] },
    { id: 10, text: 'What is the date of your most important race?', type: 'date'}
  ];