$(document).ready(() => {

  const chatrooms = (utils) => {
    /*
     * Perform a post request to send a message in the chatroom.
    **/
    const postMessageToChatroom = (chatroomId, content) => {
      return utils.post(`/chatroom/${chatroomId}/message`, { content });
    }

    /*
     * Perform a post request to include the user as a member in the chatroom.
    **/
    const joinChatroom = (chatroomId) => {
      return utils.post(`/chatroom/${chatroomId}/join`, {});
    }

    /*
     * Perform a post request to include the user as a member in the chatroom.
    **/
    const leaveChatroom = (chatroomId) => {
      return utils.post(`/chatroom/${chatroomId}/leave`, {});
    }

    return {
      postMessageToChatroom,
      joinChatroom,
      leaveChatroom,
    };
  }

  const utils = () => {
    const DEFAULT_HEADERS = { 'Content-Type': 'application/json' }

    const post = async (url, headers, body) => {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          ...DEFAULT_HEADERS,
          ...headers
        },
        ...body
      });
      return response.json();
    }

    const get = async (url, headers) => {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          ...DEFAULT_HEADERS,
          ...headers
        }
      });
      return response.json();
    }
     
    return {
      post,
      get
    }
  }

  const _utils = utils();

  const exports = {
    utils: _utils,
    chatrooms: chatrooms(_utils),
  }

  window.chattenge = exports;
});
