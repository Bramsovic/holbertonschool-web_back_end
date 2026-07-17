import redis from 'redis';

const client = redis.createClient();
const channel = 'holberton school channel';

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.on('message', (chan, message) => {
  if (chan === channel) {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe(channel);
      client.quit();
    }
  }
});

client.subscribe(channel);
