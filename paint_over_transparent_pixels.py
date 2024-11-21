{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "623f6c63-1f7a-47bc-80fe-d64caf128fad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: Pillow in c:\\users\\user\\anaconda3\\envs\\my_enviroments\\lib\\site-packages (10.4.0)\n",
      "Формат изображения: PNG\n",
      "Изображение содержит прозрачные пиксели. Изменяем их на белые.\n",
      "Изображение сохранено как: 2bc0784868937b62f92068cb2836d861_processed.png\n",
      "Изображение успешно обработано и сохранено как 'processed_image.png'.\n"
     ]
    }
   ],
   "source": [
    "!pip install Pillow\n",
    "from PIL import Image\n",
    "def process_image(file_path):\n",
    "    image = Image.open(file_path)\n",
    "    print(f\"Формат изображения: {image.format}\")\n",
    "    if image.format == 'PNG':\n",
    "        if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):\n",
    "            print(\"Изображение содержит прозрачные пиксели. Изменяем их на белые.\")\n",
    "            new_image = Image.new(\"RGBA\", image.size, (255, 255, 255, 255))\n",
    "            new_image.paste(image, (0, 0), image)\n",
    "            new_image = new_image.convert(\"RGB\")\n",
    "            new_image.save(file_path.replace('.png', '_processed.png'), 'PNG')\n",
    "            print(\"Изображение сохранено как:\", file_path.replace('.png', '_processed.png'))\n",
    "        else:\n",
    "            print(\"Изображение не содержит прозрачных пикселей.\")\n",
    "    else:\n",
    "        print(\"Изображение не в формате PNG. Загружается как есть.\")\n",
    "        image.save(file_path.replace('.jpg', '_processed.jpg'), 'JPEG')\n",
    "        print(\"Изображение сохранено как:\", file_path.replace('.jpg', '_processed.jpg'))\n",
    "process_image('2bc0784868937b62f92068cb2836d861.png')\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5db7db97-6284-4ff0-ba30-5569998b14c2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
