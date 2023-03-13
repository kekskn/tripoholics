import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  dialogs: [],
  currentDialog: {
    companion: undefined,
    dialogId: undefined,
    isLoading: false,
    messages: undefined,
  },
};

const chatSlice = createSlice({
  name: "chat",
  initialState,
  reducers: {
    setDialogs: (state, { payload }) => {
      state.dialogs = payload;
    },
    setCurrentDialog: (state, { payload }) => {
      state.currentDialog = {
        ...state.currentDialog,
        companion: payload.companion,
        dialogId: payload.dialogId,
        messages: undefined,
      };
    },
    fetchDialog: (state) => {
      state.currentDialog = {
        ...state.currentDialog,
        messages: undefined,
        isLoading: true,
      };
    },
    setMessages: (state, { payload }) => {
      state.currentDialog = {
        ...state.currentDialog,
        messages: payload,
        isLoading: false,
      };
    },
    addNewMessage: (state, { payload }) => {
      state.currentDialog.messages = [...state.currentDialog.messages, payload];
    },
  },
});

export default chatSlice;
