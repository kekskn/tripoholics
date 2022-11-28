import React, { useEffect, useState } from "react";

import smileIcon from "../../../../static/photos/icons/smile.png";
import addFileIcon from "../../../../static/photos/icons/paper-clip.png";
import sendIcon from "../../../../static/photos/icons/send.png";
import microIcon from "../../../../static/photos/icons/microphone.png";

import "./MessageInputBlock.scss";
// import blockHeightCalc from "src/utils/blockHeightCalc";
import blockHeightCalc from "../../../utils/blockHeightCalc";

export default function MessageInputBlock({ onChangeHeight }) {
  const [inputValue, setInputValue] = useState("");

  const onInputChange = (e) => {
    setInputValue(e.target.value);
  };

  useEffect(() => {
    onChangeHeight(blockHeightCalc(".chat__input-block"));
  }, []);

  return (
    <div className="message-input-block">
      <div className="message-input-block__field">
        <input
          type="text"
          placeholder="Напишите сообщение..."
          value={inputValue}
          onChange={onInputChange}
        />
        <div className="message-input-block__icon">
          <img
            src={smileIcon}
            style={{ width: "20px", height: "20px" }}
            alt=""
          />
        </div>
        <div className="message-input-block__icon">
          <img
            src={addFileIcon}
            style={{ width: "20px", height: "20px" }}
            alt=""
          />
        </div>
        <div className="message-input-block__icon">
          <img
            src={microIcon}
            style={{ width: "20px", height: "20px" }}
            alt=""
          />
        </div>
      </div>
      <div className="message-input-block__send">
        <img
          src={sendIcon}
          style={{ width: "16px", height: "16px" }}
          alt="send text message"
        />
      </div>
    </div>
  );
}
