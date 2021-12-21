{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled39.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOGYIzLnyP15HM/xZsw2PSc",
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
        "<a href=\"https://colab.research.google.com/github/SananSuleymanov/Translation_and_Rotation/blob/main/Translation%20and%20Rotation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "VSFcfchEHPLh"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "A = np.array([3., 6., 9.])\n",
        "B = np.array([6., 4., 2.])\n",
        "C = np.array([3., 6., 9.])"
      ],
      "metadata": {
        "id": "wkBg-3oSJe51"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "xaxis = np.array([1., 0., 0.,])\n",
        "yaxis = np.array([0., 1., 0.,])\n",
        "zaxis = np.array([0., 0., 1.,])"
      ],
      "metadata": {
        "id": "jmgvY8fMKbQB"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "I = np.array([[1., 0., 0.],\n",
        "              [0., 1., 0.],\n",
        "              [0., 0., 1.]])"
      ],
      "metadata": {
        "id": "4i4tikSlKunh"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "R2= I + np.sin(2*np.pi/3)*yaxis + (1 - np.cos(2*np.pi/3))*np.dot(yaxis, yaxis)"
      ],
      "metadata": {
        "id": "uIGbrwVrNYNw"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def v_cross(v):\n",
        "  return np.array([[0., -v[2], v[1]],\n",
        "                   [v[2], 0., -v[0]],\n",
        "                   [-v[1], v[0], 0.,]])"
      ],
      "metadata": {
        "id": "Tuyg3q2YOApT"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def rotate(ax, angle):\n",
        "  v_x = v_cross(ax)\n",
        "  return I + np.sin(angle)*v_x + (1 - np.cos(angle))*np.matmul(v_x, v_x)\n"
      ],
      "metadata": {
        "id": "6SG50Fp6SwZK"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "r1 = np.matmul(rotate(xaxis, np.pi/4), A)\n",
        "r2 = np.matmul(rotate(xaxis, np.pi/4), B)\n",
        "r3 = np.matmul(rotate(xaxis, np.pi/4), C)"
      ],
      "metadata": {
        "id": "h-SMrHqeUDj5"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(r1, r2, r3) #rotation around X axis"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "_mM07K9rZ8h5",
        "outputId": "0bc9d66a-d110-477f-d927-8a4f9660fded"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[ 3.         -2.12132034 10.60660172] [6.         1.41421356 4.24264069] [ 3.         -2.12132034 10.60660172]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "r21 = np.matmul(rotate(yaxis, 2*np.pi/3), r1)\n",
        "r22 = np.matmul(rotate(yaxis, 2*np.pi/3), r2)\n",
        "r23 = np.matmul(rotate(zaxis, 2*np.pi/3), r3)"
      ],
      "metadata": {
        "id": "GUtI5rn7Usq2"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(r21, r22, r23) #rotation around Y axis"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "w78tjHb1aI1F",
        "outputId": "d799c571-8f6e-4290-9db8-61693c7f2fc3"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[ 7.68558654 -2.12132034 -7.90137707] [ 0.67423461  1.41421356 -7.31747277] [ 0.33711731  3.65873638 10.60660172]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "T = np.array([[1., 0., 0., 0.],\n",
        "              [0., 1., 0., 0.],\n",
        "              [0., 0., 1., -3.],\n",
        "              [0., 0., 0., 1.]])"
      ],
      "metadata": {
        "id": "RMj-3IeXVDaK"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t1= np.array([r21[0],\n",
        "              r21[1],\n",
        "              r21[2],\n",
        "              1.])\n",
        "t2= np.array([r22[0],\n",
        "              r22[1],\n",
        "              r22[2],\n",
        "              1.])\n",
        "t3= np.array([r23[0],\n",
        "              r23[1],\n",
        "              r23[2],\n",
        "              1.])"
      ],
      "metadata": {
        "id": "ubcAYm6eWYSh"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "r21_t = np.matmul(T, t1)\n",
        "r22_t = np.matmul(T, t2)\n",
        "r23_t = np.matmul(T, t3)"
      ],
      "metadata": {
        "id": "L0E2eje9WzeE"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(r21_t, r22_t, r23_t) #translation along Z axis"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "2Ohu3nSxZxcH",
        "outputId": "d52a2ee5-3d23-4f79-b31a-281eb67c10e6"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[  7.68558654  -2.12132034 -10.90137707   1.        ] [  0.67423461   1.41421356 -10.31747277   1.        ] [0.33711731 3.65873638 7.60660172 1.        ]\n"
          ]
        }
      ]
    }
  ]
}