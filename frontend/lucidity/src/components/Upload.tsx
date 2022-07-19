import axios from "axios";
import React, { useState } from "react";
import "./Upload.css";
import { useNavigate } from "react-router-dom";
import { PulseSpinner, StageSpinner } from "react-spinners-kit";

type UploadProp = {
  user: User | null;
  setUser: React.Dispatch<React.SetStateAction<User | null>>;
};

let Upload = ({ user, setUser }: UploadProp) => {
  const [fileToUpload, setFile] = useState(null);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  let onFileChange = (event: any) => {
    setFile(event.target.files[0]);
  };

  let onFileUpload = async (event: any) => {
    // let id = user.id;
    if (user === null) {
      return;
    }

    let id = user._id;
    let checked: string[] = [];
    let checkboxes: NodeList = document.querySelectorAll<HTMLInputElement>(
      "input[type='checkbox']"
    );
    let checkboxArray: Array<HTMLInputElement> =
      Array.prototype.slice.call(checkboxes);
    checkboxArray.forEach((checkbox: HTMLInputElement) => {
      if (checkbox.checked) {
        checked.push(checkbox.value);
      }
    });
    await axios
      .post(
        "/upload",
        { inputFile: fileToUpload },
        { headers: { "Content-Type": "multipart/form-data" } }
      )
      .then((response) => {
        setLoading(true);
        console.log(response.data);
      });
    axios
      .post(
        "/analysistypes",
        { dataList: checked, userID: id },
        { headers: { "Content-Type": "application/json" } }
      )
      .then((response) => {
        const user: User = response.data as User;
        setUser(user);
        console.log("user", user);
      })
      .then(() => {
        setLoading(false);
        navigate("/wrapped");
      });
  };

  return (
    <div className="upload-page-container">
      <div className="upload-left">
        <div className="upload-left__title">Upload File</div>
        <div className="upload-left__subtitle">
          Navigate to the Facebook "Download Your Information" page, select the
          appropriate date range, "JSON" as the Format, "Low" for Media Quality,
          then in the list below that, Deselect All and check only Posts,
          Comments, and Messages. Then click on "Create File", and when it
          arrives via email, select the file once you receive and download it.
        </div>

        <label className="upload-left__upload">
          <input
            type="file"
            onChange={(event) => onFileChange(event)}
            className="upload-button"
            accept=".zip,.txt"
          />
          Upload Here
        </label>
      </div>
      <div className="upload-right">
        <div className="upload-right__title">Features:</div>
        <div className="upload-right__subtitle">
          Select the features you would like to see. <br />
          Different selections will vary in the data used.
        </div>
        <div className="upload-right__checkbox-container">
          <div className="checkbox-item">
            <input type="checkbox" id="emoji" value="emoji" />
            <label htmlFor="emoji">Emoji Usage</label>
          </div>
          <div className="checkbox-item">
            <input
              type="checkbox"
              id="messaging_profile"
              value="messaging_profile"
            />
            <label htmlFor="messaging_profile">Messaging Profile</label>
          </div>

          <div className="checkbox-item">
            <input type="checkbox" id="response_time" value="response_time" />
            <label htmlFor="response_time">Response Time</label>
          </div>

          <div className="checkbox-item">
            <input type="checkbox" id="emotions" value="emotions" />
            <label htmlFor="emotions">Emotions</label>
          </div>

          <div className="checkbox-item">
            <input type="checkbox" id="topics" value="topics" />
            <label htmlFor="topics">Topics</label>
          </div>

          <div className="checkbox-item">
            <input type="checkbox" id="personality" value="personality" />
            <label htmlFor="personality">Personality</label>
          </div>

          <div className="checkbox-item">
            <input type="checkbox" id="celeb_matches" value="celeb_matches" />
            <label htmlFor="celeb_matches">Celebrity Matches</label>
          </div>

          <div className="checkbox-item">
            <input type="checkbox" id="word_freqs" value="word_freqs" />
            <label htmlFor="word_freqs">Word Frequency</label>
          </div>
        </div>
        <button
          className="upload-right__btn"
          onClick={(event) => onFileUpload(event)}
        >
          Submit
        </button>
        <div className="centered">
          <StageSpinner
            size={100}
            color="#000"
            loading={loading}
          ></StageSpinner>
        </div>
      </div>
    </div>
  );
};

export default Upload;
