import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];

function getItemById(id) {
  return listProducts.find((item) => item.id === Number(id));
}

function reserveStockById(itemId, stock) {
  redisClient.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  return getAsync(`item.${itemId}`);
}

function formatProduct(item, currentQuantity = item.stock) {
  return {
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity,
  };
}

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

app.get('/list_products', (request, response) => {
  response.json(listProducts.map((item) => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
  })));
});

app.get('/list_products/:itemId', async (request, response) => {
  const item = getItemById(request.params.itemId);

  if (!item) {
    response.json({ status: 'Product not found' });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(item.id);
  const currentQuantity = reservedStock === null ? item.stock : Number(reservedStock);

  response.json(formatProduct(item, currentQuantity));
});

app.get('/reserve_product/:itemId', async (request, response) => {
  const item = getItemById(request.params.itemId);

  if (!item) {
    response.json({ status: 'Product not found' });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(item.id);
  const currentQuantity = reservedStock === null ? item.stock : Number(reservedStock);

  if (currentQuantity < 1) {
    response.json({
      status: 'Not enough stock available',
      itemId: item.id,
    });
    return;
  }

  reserveStockById(item.id, currentQuantity - 1);

  response.json({
    status: 'Reservation confirmed',
    itemId: item.id,
  });
});

app.listen(port);
