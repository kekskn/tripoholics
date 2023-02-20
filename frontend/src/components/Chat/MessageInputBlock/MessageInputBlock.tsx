import React, { useEffect, useState } from "react";

// import data from "@emoji-mart/data";
// import { Picker } from "emoji-mart";

import data from "@emoji-mart/data";
// import Picker from "@emoji-mart/react";

import smileIcon from "../../../../static/photos/icons/smile.png";
import addFileIcon from "../../../../static/photos/icons/paperclip.png";
import sendIcon from "../../../../static/photos/icons/send.png";
import microIcon from "../../../../static/photos/icons/microphone.png";

import "./MessageInputBlock.scss";
// import blockHeightCalc from "src/utils/blockHeightCalc";
import blockHeightCalc from "../../../utils/blockHeightCalc";

export default function MessageInputBlock({ onChangeHeight }) {
  const [inputValue, setInputValue] = useState("");
  const [isWrittenMessage, setIsWrittenMessage] = useState(false);
  // new Picker({
  //   data: async () => {
  //     const response = await fetch(
  //       "https://cdn.jsdelivr.net/npm/@emoji-mart/data"
  //     );

  //     return response.json();
  //   },
  // });
  const onInputChange = (e) => {
    if (e.target.value && !isWrittenMessage) setIsWrittenMessage(true);
    if (!e.target.value) setIsWrittenMessage(false);
    setInputValue(e.target.value);
  };

  useEffect(() => {
    onChangeHeight(blockHeightCalc(".chat__input-block"));
  }, []);

  const onSendMessage = () => {
    console.log("onSendMessage");
    setInputValue("");
  };

  const addEmoji = (e) => {
    let emoji = e.native;
    setInputValue(inputValue + emoji);
  };

  return (
    <div className="message-input-block">
      <div className="message-input-block__field">
        <span>
          {/* <Picker onSelect={addEmoji} /> */}
          {/* <Picker data={data} onEmojiSelect={console.log} /> */}
          {/* <EmojiPicker /> */}
        </span>
        <div className="message-input__left-btns">
          <button className="message-input__btn smile-btn">
            <img src={smileIcon} alt="" />
          </button>
          <button className="message-input__btn file-btn">
            <img src={addFileIcon} alt="" />
          </button>
        </div>
        <input
          className="message-input"
          type="text"
          placeholder="Напишите сообщение..."
          value={inputValue}
          onChange={onInputChange}
        />
        <div className="message-input__right-btns">
          {/* {isWrittenMessage ? ( */}
          <button
            className="message-input__btn send-btn"
            onClick={onSendMessage}
          >
            <img src={sendIcon} alt="" />
          </button>
          {/* ) : (
            <button className="message-input__btn micro-btn">
              <img src={microIcon} alt="" />
            </button>
          )} */}
        </div>
      </div>
      {/* <button className="message-input-block__send">
        <img
          src={sendIcon}
          style={{ width: "16px", height: "16px" }}
          alt="send text message"
          onClick={onSendMessage}
        />
      </button> */}
    </div>
  );
}
