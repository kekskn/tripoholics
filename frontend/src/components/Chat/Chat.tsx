import { useParams } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";

import axios from "axios";
import "./Chat.scss";
import DialogsList from "./DialogsList/DialogsList";
import MessagesBlock from "./MessagesBlock/MessagesBlock";
import EmptyChat from "./MessagesBlock/EmptyChat/EmptyChat";
import { onLoad, setUserInfo } from "../../redux/actions";

import { hidden } from "visibilityjs";

export default function Chat() {
  const { dialogId, newDialogId } = useParams();

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
