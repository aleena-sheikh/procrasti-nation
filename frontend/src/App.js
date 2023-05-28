import './styles.css';
import React, { useState } from 'react';

function App() {
  const [income, setIncome] = useState('');
  const [age, setAge] = useState('');
  const [retirementAge, setRetirementAge] = useState('');
  const [city, setCity] = useState('');
  const [info, setInfo] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIncome(e.target.elements.income.value);
    setAge(e.target.elements.age.value);
    setRetirementAge(e.target.elements.retirementAge.value);
    setCity(e.target.elements.city.value);

    try {
      const response = await fetch("http://localhost:5000/", { method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ "income": income, "age":age, "city": city, "retirementAge":retirementAge }), });
      const data = await response.json(); // Extract JSON data from the response
      setInfo(Object.values(data)[0]);
      console.log(data) // Set the extracted data in the state
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div>
      <h1 className='title'>S(ai)vvy Savings</h1>
      <form onSubmit={handleSubmit} className="obBox">
        <input type="number" name="income" placeholder="Income" className="formField" /><br />
        <input type="number" name="age" placeholder="Age" className="formField" /><br />
        <input type="number" name="retirementAge" placeholder="Retirement Age" className="formField" /><br />
        <input type="text" name="city" placeholder="city of residence" className="formField" /><br />
        <br />
        <input type="submit" value="Submit" className="submit-button" />
      </form>
      <div className='obBox1'>
        <h2 className='returntext'>{info}</h2>
        {/* <h2>Age: {age}</h2>
        <h2>Retirement Age: {retirementAge}</h2>
        <h2>City: {city}</h2> */}
      </div>
    </div>
  );
}

export default App;
