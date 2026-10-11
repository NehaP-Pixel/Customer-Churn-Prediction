{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c14c5015-1c6a-40ff-bc27-220bd1475214",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "146ab885-5c45-46a4-90d6-5ccedbd99f3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(r\"C:\\Users\\DELL\\OneDrive\\Desktop\\customer-churn-ml\\data\\raw\\customer_churn.csv\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "845bbb61-bb7d-40ff-84a5-0f4049d2624b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ac74c8f-7a3a-4e5a-9bc8-ec65e115c5e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler = StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fbad0944-2267-4afc-96fd-eb317515dfb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#df_scaled = df_encoded.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "52c3ebe7-9d1f-44fa-8f2f-57df4451adbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#df_scaled = df_encoded.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4f9ae717-1ed0-44e3-914a-10df48b93983",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_scaled' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[15]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m df_scaled[features_to_scale] = scaler.fit_transform(\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m     df_scaled[features_to_scale]\n\u001b[32m      3\u001b[39m )\n",
      "\u001b[31mNameError\u001b[39m: name 'df_scaled' is not defined"
     ]
    }
   ],
   "source": [
    "df_scaled[features_to_scale] = scaler.fit_transform(\n",
    "    df_scaled[features_to_scale]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07580530-f6dc-431f-9167-04d61745e735",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_scaled[features_to_scale].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0dc9c6c-27d8-4340-9e65-e1174ba3e155",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(df_scaled[features_to_scale].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e64a4ab-6284-46e2-ad8b-eb7d18e5325f",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(df_scaled[features_to_scale].std())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15eb984a-ceee-4188-bc45-c39cc5a9be18",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df_scaled.drop(columns=[\"Churn\"])\n",
    "y = df_scaled[\"Churn\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a6dc8e31-79ae-43a8-a181-bb23f41f2605",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'X' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[16]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m sklearn.model_selection \u001b[38;5;28;01mimport\u001b[39;00m train_test_split\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m X_train, X_test, y_train, y_test = train_test_split(\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m     X,\n\u001b[32m      5\u001b[39m     y,\n\u001b[32m      6\u001b[39m     test_size=\u001b[32m0.20\u001b[39m,\n\u001b[32m      7\u001b[39m     random_state=\u001b[32m42\u001b[39m,\n",
      "\u001b[31mNameError\u001b[39m: name 'X' is not defined"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X,\n",
    "    y,\n",
    "    test_size=0.20,\n",
    "    random_state=42,\n",
    "    stratify=y\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8d40d7f-9343-47dd-9fac-7f90ce93b85a",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"X_train:\", X_train.shape)\n",
    "print(\"X_test:\", X_test.shape)\n",
    "print(\"y_train:\", y_train.shape)\n",
    "print(\"y_test:\", y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "597fe0b2-b00c-4c1c-843b-da712d12f495",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Training Churn Distribution:\")\n",
    "print(y_train.value_counts())\n",
    "\n",
    "print(\"\\nTesting Churn Distribution:\")\n",
    "print(y_test.value_counts())"
   ]
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
   "version": "3.14.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
