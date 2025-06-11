export default function Question({ data, value, onChange }) {
    const { type, options, text, id } = data
  
    if (type === 'date') {
      return (
        <label>
          {text}
          <input
            type="date"
            value={value || ''}
            onChange={e => onChange(e.target.value)}
          />
        </label>
      )
    }
  
    if (type === 'select') {
      return (
        <label>
          {text}
          <select
            value={value || ''}
            onChange={e => onChange(e.target.value)}
          >
            <option value="" disabled>Select…</option>
            {options.map(opt => (
              <option key={opt} value={opt}>{opt}</option>
            ))}
          </select>
        </label>
      )
    }

    if (type === 'time') {
        return (
          <label>
            {text}
            <input
              type="time"
              value={value || ''}
              onChange={e => onChange(e.target.value)}
            />
          </label>
        )
      }
  
          {options.includes('Enter:') && value === 'Enter:' && (
            <label>
              <input
                type="text"
                value={valueDetail || ''}
                onChange={e => onChange(e.target.value)}
              />
            </label>
          )}
  
    return null
  }