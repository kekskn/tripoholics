import React, { useState, useRef, useEffect } from "react";
import MessageInputBlock from "../MessageInputBlock/MessageInputBlock";
import MessageItem from "../MessageItem/MessageItem";
import "./MessagesBlock.scss";

export default function MessagesBlock() {
  const [inputBlockHeight, setInputBlockHeight] = useState("");
  const messagesBlockRef = useRef<any>();
  const onChangeHeight = (height) => {
    setInputBlockHeight(`${height}px`);
  };

  useEffect(() => {
    if (messagesBlockRef.current) {
      messagesBlockRef.current.scrollTo(
        0,
        messagesBlockRef.current.scrollHeight
      );
    }
  }, []);

  return (
    <div className="chat__main-block">
      <div className="chat__main-block-wrapper">
        <div
          className="chat__messages-block"
          style={{ bottom: inputBlockHeight }}
          ref={messagesBlockRef}
        >
          <MessageItem isMy={false} isOnline isRead />
          <MessageItem isMy isOnline={false} isRead />
          <MessageItem isMy={false} isOnline isRead />
          <MessageItem isMy isOnline={false} isRead />
          <MessageItem isMy={false} isOnline isRead />
          <MessageItem isMy isOnline={false} isRead />
          <MessageItem isMy={false} isOnline isRead />
          <MessageItem isMy isOnline={false} isRead />
          <MessageItem isMy={false} isOnline isRead />
          <MessageItem isMy isOnline={false} isRead />
          <MessageItem isMy={false} isOnline isRead />
        </div>
      </div>
      <div className="chat__input-block">
        <MessageInputBlock onChangeHeight={onChangeHeight} />
      </div>
    </div>
  );
}
