import React, { useState, useMemo, useRef ,useEffect} from 'react'
import TinderCard from 'react-tinder-card'
import axios from "axios";
import '../App.css';

var db = []

function DogSwipe () {
    const [currentIndex, setCurrentIndex] = useState(0)
    const [lastDirection, setLastDirection] = useState()
    // used for outOfFrame closure
    const currentIndexRef = useRef(currentIndex)
    const [size, setSize] = useState(0)

    //Fetch data
    useEffect(() => {
        axios
      .get("/api/dogs/")
      .then((res) => {
        var dogs = res.data
        for(var i = 0; i < dogs.length; i++){
            db[i] = {name: dogs[i].name, url: JSON.parse(dogs[i].images)[0]}
        }
        setSize(db.length)
        setCurrentIndex(db.length - 1)
        })
      .catch((err) => console.log(err))
    },[]);
   
  
    const childRefs = useMemo(
      () =>
        Array(size)
          .fill(0)
          .map((i) => React.createRef()),
      [size]
    )
  
    const updateCurrentIndex = (val) => {
      setCurrentIndex(val)
      currentIndexRef.current = val
    }
  
    const canGoBack = currentIndex < size - 1
  
    const canSwipe = currentIndex >= 0
  
    // set last direction and decrease current index
    const swiped = (direction, nameToDelete, index) => {
      setLastDirection(direction)
      updateCurrentIndex(index - 1)
    }
  
    const outOfFrame = (name, idx) => {
      currentIndexRef.current >= idx && childRefs[idx].current.restoreCard()
    }
  
    const swipe = async (dir) => {
      if (canSwipe && currentIndex < size) {
        await childRefs[currentIndex].current.swipe(dir) // Swipe the card!
      }
    }
  
    // increase current index and show card
    const goBack = async () => {
      if (!canGoBack) return
      const newIndex = currentIndex + 1
      updateCurrentIndex(newIndex)
      await childRefs[newIndex].current.restoreCard()
    }
  
    return (
      <div className='dogswipe'>
        <link
          href='https://fonts.googleapis.com/css?family=Damion&display=swap'
          rel='stylesheet'
        />
        <link
          href='https://fonts.googleapis.com/css?family=Alatsi&display=swap'
          rel='stylesheet'
        />
        <h1>Fur-Ever</h1>
        <div className='cardContainer'>
          {db.map((character, index) => (
            <TinderCard
              ref={childRefs[index]}
              className='swipe'
              key={character.name}
              onSwipe={(dir) => swiped(dir, character.name, index)}
              onCardLeftScreen={() => outOfFrame(character.name, index)}
            >
              <div
                className='card'
                style={{ backgroundImage: 'url(' + character.url + ')' }}
              >
                <h3>{character.name}</h3>
              </div>
            </TinderCard>
          ))}
        </div>
        <div className='buttons'>
          <button style={{ backgroundColor: !canSwipe && '#c3c4d3' }} onClick={() => swipe('left')}>Swipe left!</button>
          <button style={{ backgroundColor: !canGoBack && '#c3c4d3' }} onClick={() => goBack()}>Undo swipe!</button>
          <button style={{ backgroundColor: !canSwipe && '#c3c4d3' }} onClick={() => swipe('right')}>Swipe right!</button>
        </div>
        {lastDirection ? (
          <h2 key={lastDirection} className='infoText'>
            You swiped {lastDirection}
          </h2>
        ) : (
          <h2 className='infoText'>
            Swipe right to match and left to pass.
          </h2>
        )}
      </div>
    )
  }
  
  export default DogSwipe