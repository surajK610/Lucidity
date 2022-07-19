import React from 'react';
import ReactWordcloud from 'react-wordcloud';
import { Resizable } from "re-resizable";
import './WordCloud.css'

const resizeStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  border: "solid 1px #ddd",
  background: "#f9fff6"
};
const options : any = {
  colors: ["374C2D", "#5F9A44", "#C6FFAD",  "#36A403", "#214A0D"],
  fontFamily: "sans-serif",
  fontSizes: [10, 80],
  fontStyle: "normal",
  fontWeight: "bold",
  padding: 1,
  rotations: 2,
  rotationAngles: [0, 90],
  transitionDuration: 1000
};

type Word  = {
  text : string;
  value : number
}

type WordCloudProp = {
  words : Word[]
}
let WordCloud = ({words} : WordCloudProp) => { 
  return (
    <div className="container-wordcloud">
      <div className="text-container">
        <h1 className="response__average">Word Cloud Fun ;)</h1>
        <div className="cloud_description">
          Play with some of your most used words. Try reshaping the box!
        </div>
        <div className="container-resizable">
          <Resizable defaultSize={{ width: 800, height: 400}} style={resizeStyle}>
          <div style={{ width: "100%", height: "100%" }}>
            <ReactWordcloud options={options} words={words} />
          </div>
          </Resizable>
        </div>
      </div>
    </div>
  )
}

export default WordCloud