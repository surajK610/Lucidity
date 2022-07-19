import React from 'react';
import './CelebrityBox.css';

type CelebrityBoxProp = {
  name: string;
  matchPercent: string;
  imgPath: string;
};

let CelebrityBox = ({ name, matchPercent, imgPath}: CelebrityBoxProp) => {

  return (
    <div className="celebbox">
        <img src={require(`../images/${imgPath}`)}alt="BM"/>
        <h1 className="celebbox-h1">{name}</h1>
        <h1 className="celebbox-h1">{matchPercent} Match</h1>
    </div>
  );
};

export default CelebrityBox;
