import React from "react";
import MessageItem from "../MessageItem/MessageItem";
import "./MessagesBlock.scss";

export default function MessagesBlock() {
  return (
    <div className="chat__messages-block">
      <MessageItem isMy={false} isOnline isRead />
      <MessageItem isMy isOnline={false} isRead />
      <MessageItem isMy={false} isOnline isRead />
      <MessageItem isMy isOnline={false} isRead />
      <MessageItem isMy={false} isOnline isRead />
    </div>
  );
}
