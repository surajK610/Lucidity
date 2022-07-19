import React, { useState, useEffect } from "react";
import ReactFullpage from "@fullpage/react-fullpage";
import Emoji from "./Emoji";
import CelebrityComparison from "./CelebrityComparison";
import Response from "./Response";
import WordCloud from "./WordCloud";
import Statistics from "./Statistics";
import Personality from "./Personality";
import Topics from "./Topics";
import words from "./words";
import { TableOfContents } from "react-table-of-contents";
import { useNavigate } from "react-router-dom";
import Emotions from "./Emotions";
import "./FullPage.css";

type FullPageProp = {
  user: User;
};

const userDataParts: string[] = [
  "messaging_profile",
  "emoji",
  "emotions",
  "response_time",
  "topics",
  "celeb_matches",
  "word_freqs",
  "personality",
];

const possibleSectionNames: string[] = [
  "statistics",
  "emojis",
  "emotions",
  "responses",
  "topics",
  "celebrities",
  "words",
  "personality",
];

const FullPage = ({ user }: FullPageProp) => {
  const navigate = useNavigate();

  const [sectionNames, setSectionNames] = useState<string[]>([]);

  useEffect(() => {
    console.log("user is null");
    if (user === null) {
      navigate("/login");
    } else {
      const newSectionNames: string[] = [];

      userDataParts.forEach((dataPart, index) => {
        if (user.dataList.includes(dataPart)) {
          newSectionNames.push(possibleSectionNames[index]);
        }
      });

      setSectionNames(newSectionNames);
    }
  }, [user]);

  return (
    <>
      {user && (
        <div className="full-page-container">
          <ReactFullpage
            //fullpage options
            licenseKey={"YOUR_KEY_HERE"}
            scrollingSpeed={1000} /* Options here */
            render={({ state, fullpageApi }) => {
              return (
                <ReactFullpage.Wrapper>
                  {user.dataList.includes("messaging_profile") ? (
                    <div id="statistics" className="section">
                      <Statistics
                        averageTextLength={user.avgTextLength}
                        totalMessages={user.totalMessages}
                        convoInitFreq={user.convoInitFreq}
                        msgSentiment={user.msgSentiment.positive}
                      ></Statistics>
                    </div>
                  ) : null}
                  {user.dataList.includes("emoji") ? (
                    <div id="emojis" className="section">
                      <Emoji
                        mostUsedEmojis={user.favEmojis}
                        users={user.emojisByContact}
                      ></Emoji>
                    </div>
                  ) : null}
                  {user.dataList.includes("emotions") ? (
                    <div id="emotions" className="section">
                      <Emotions emotionList={user.emotions}></Emotions>
                    </div>
                  ) : null}
                  {user.dataList.includes("response_time") ? (
                    <div id="responses" className="section">
                      <Response
                        avgResponseTime={user.avgResponseTime}
                        responseUsers={user.contactResTimes}
                      ></Response>
                    </div>
                  ) : null}
                  {user.dataList.includes("topics") ? (
                    <div id="topics" className="section">
                      <Topics topicList={user.topics}></Topics>
                    </div>
                  ) : null}
                  {user.dataList.includes("celeb_matches") ? (
                    <div id="celebrities" className="section">
                      <CelebrityComparison
                        celebrities={user.celebMatches}
                      ></CelebrityComparison>
                    </div>
                  ) : null}
                  {user.dataList.includes("word_freqs") ? (
                    <div id="words" className="section">
                      <WordCloud words={user.wordFreqs}></WordCloud>
                    </div>
                  ) : null}
                  {user.dataList.includes("personality") ? (
                    <div id="personality" className="section">
                      <Personality personality={user.personality}></Personality>
                    </div>
                  ) : null}
                </ReactFullpage.Wrapper>
              );
            }}
          />{" "}
          <div className="table-contents">
            {sectionNames.map((sectionName) => (
              <a className="content-link" href={`#${sectionName}`}>
                <div className="content-link-text">{sectionName}</div>
              </a>
            ))}
          </div>
        </div>
      )}
    </>
  );
};

export default FullPage;
