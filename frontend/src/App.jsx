import { useEffect, useState } from 'react'

function App() {
  const [country, setCountry] = useState(null)

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/countries/random')
      .then(response => response.json())
      .then(data => setCountry(data))
      .catch(error => console.error(error))
  }, [])

  if (!country) {
    return <p>Loading...</p>
  }

  return (
    <div>
      <h1>Geography Game</h1>

      <h2>{country.name}</h2>
      <p>Country code: {country.code}</p>

      <h3>Ranks</h3>

      <p>Population: #{country.ranks.population}</p>
      <p>Area: #{country.ranks.area}</p>
      <p>GDP per capita: #{country.ranks.gdp_per_capita}</p>
      <p>Tourism: #{country.ranks.tourism}</p>
      <p>Fertility: #{country.ranks.fertility}</p>
      <p>Life expectancy: #{country.ranks.life_expectancy}</p>
      <p>Emissions per capita: #{country.ranks.emissions_per_capita}</p>
      <p>Cuisine: #{country.ranks.cuisine}</p>
      <p>Internet usage: #{country.ranks.internet_usage}</p>
    </div>
  )
}

export default App