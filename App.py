{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOIvE+M5pSulxylMt3RiaVg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/afrian2416/Reader/blob/main/App.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "def scrape_website(url):\n",
        "    try:\n",
        "        response = requests.get(url)\n",
        "        soup = BeautifulSoup(response.content, 'html.parser')\n",
        "\n",
        "        title = soup.find(class_='entry-title')\n",
        "        content = soup.find(class_='entry-content')\n",
        "\n",
        "        if title and content:\n",
        "            return {\n",
        "                'title': title.get_text(strip=True),\n",
        "                'content': content.get_text(strip=True)\n",
        "            }\n",
        "        else:\n",
        "            return None\n",
        "    except Exception as e:\n",
        "        st.error(f\"Error occurred: {str(e)}\")\n",
        "        return None\n",
        "\n",
        "st.title('Web Scraper')\n",
        "\n",
        "url = st.text_input('Enter the URL to scrape:')\n",
        "\n",
        "if st.button('Scrape'):\n",
        "    if url:\n",
        "        result = scrape_website(url)\n",
        "        if result:\n",
        "            st.subheader('Scraped Data:')\n",
        "            st.write(f\"Title: {result['title']}\")\n",
        "            st.write('Content:')\n",
        "            st.text_area('', value=result['content'], height=300)\n",
        "        else:\n",
        "            st.warning('Could not find the specified elements on the page.')\n",
        "    else:\n",
        "        st.warning('Please enter a URL.')"
      ],
      "metadata": {
        "id": "HiUCBDdXUAgf"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}