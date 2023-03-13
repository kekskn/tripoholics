import { createAction } from "@reduxjs/toolkit";
import { ON_LOAD, SEND_NEW_MESSAGE, GET_CURRENT_DIALOG } from "../constants";
import chatSlice from "../reducers/chat";
import userSlice from "../reducers/user";

export const { setUserInfo } = userSlice.actions;
export const {
  setDialogs,
  setCurrentDialog,
  fetchDialog,
  setMessages,
  addNewMessage,
} = chatSlice.actions;

export const onLoad = createAction(ON_LOAD);
export const sendNewMessage = createAction(SEND_NEW_MESSAGE);
export const getCurrentDialog = createAction(GET_CURRENT_DIALOG);
