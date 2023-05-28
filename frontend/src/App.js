import './styles.css';
import React, { useState } from 'react';

function App() {
  const [income, setIncome] = useState('');
  const [age, setAge] = useState('');
  const [retirementAge, setRetirementAge] = useState('');
  const [city, setCity] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    setIncome(e.target.elements.income.value);
    setAge(e.target.elements.age.value);
    setRetirementAge(e.target.elements.retirementAge.value);
    setCity(e.target.elements.city.value);

    fetch()
  };

  return (
    <div>
      <h1>Welcome to my sdvapp</h1>
      <form onSubmit={handleSubmit} className="obBox">
        <input type="number" name="income" placeholder="Income" className="formField" /><br />
        <input type="number" name="age" placeholder="Age" className="formField" /><br />
        <input type="number" name="retirementAge" placeholder="Retirement Age" className="formField" /><br />
        <input type="text" name="city" placeholder="city of residence" className="formField" /><br />
        <br/>
        <input type="submit" value="Submit" className="largeButton" />
      </form>
      <h2>Income: {income}</h2>
      <h2>Age: {age}</h2>
      <h2>Retirement Age: {retirementAge}</h2>
      <h2>City: {city}</h2>
    </div>
  );
}

export default App;
