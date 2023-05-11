import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  isLoading: false,
  users: [],
};

const mapSlice = createSlice({
  name: "map",
  initialState,
  reducers: {
    fetchUserPopupInfo: (state, { payload }) => {
      state.isLoading = true;
    },
    setUserPopupInfo: (state, { payload }) => {
      state.isLoading = false;
      state.users = [...state.users, payload];
    },
  },
});

export default mapSlice;
