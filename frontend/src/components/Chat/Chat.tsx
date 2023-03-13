import { useParams } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";

import axios from "axios";
import "./Chat.scss";
import DialogsList from "./DialogsList/DialogsList";
import MessagesBlock from "./MessagesBlock/MessagesBlock";
import EmptyChat from "./MessagesBlock/EmptyChat/EmptyChat";
import { onLoad, setUserInfo } from "../../redux/actions";

export default function Chat() {
  const { dialogId, newDialogId } = useParams();
  // const [messages, setMessages] = useState([]);
  // const dispatch = useDispatch();
  // console.log("roomName: ", roomName);

  // async function getMessages() {
  //   await axios
  //     .get("http://127.0.0.1:8000/api/messages?dialogId=1")
  //     .then((data) => {
  //       console.log("data:", data);
  //       setMessages(data.data);
  //     });
  // }

  console.log("dialogID: ", dialogId, newDialogId);
  return (
    <div className="chat">
      <DialogsList />
      {dialogId || newDialogId ? (
        <MessagesBlock
          dialogId={dialogId ? dialogId : newDialogId}
          isNewDialog={!!newDialogId}
        />
      ) : (
        <EmptyChat isNewDialog={false} />
      )}
    </div>
  );
}
