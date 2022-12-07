import React, { useState, useMemo, useRef ,useEffect} from 'react'
import TinderCard from 'react-tinder-card'
import axios from "axios";
import '../App.css';
import '../index.css'
var db = [];
function Dogs() {
  const [size, setSize] = useState(0)
  var dogs;
  //Fetch data
  useEffect(() => {
      axios
    .get("/api/dogs/")
    .then((res) => {
      var dogs = res.data
      for(var i = 0; i < dogs.length; i++){
          db[i] = dogs[i];
      }
      setSize(db.length)
      })
    .catch((err) => console.log(err))
  },[]);

  return (
    <div className="App bg-blue-50">
      <header classname="App-header">
      {db.map((dog) => (
      <div className = "dog_container">
        <img src= {JSON.parse(dog.images)[0]} width="200" id="dog_profile"></img>
        <dog_name>{dog.name}<br/></dog_name>
          <b>Breed:</b> {dog.breed}<br/>
          <b>Sex:</b> {dog.sex}<br/>
          <b>Weight:</b> {dog.weight}<br/>
          <b>Age:</b> {dog.age}<br/>
          <b>Location:</b> {dog.location}<br/>
          <b>Attributes:</b> {JSON.parse(dog.attributes).join(", ")}<br/>
          <b>Description:</b> {dog.description}<br/>
      </div>))}
      </header>
    </div>)
}

export default Dogs;