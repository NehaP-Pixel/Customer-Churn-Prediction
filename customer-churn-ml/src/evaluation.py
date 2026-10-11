{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9eecc5eb-0f19-4dfd-8163-b8d1737e62fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e346c9c8-a75c-4910-9cf5-31f0b054c56e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Customer_ID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Location</th>\n",
       "      <th>Tenure_Months</th>\n",
       "      <th>Monthly_Charges</th>\n",
       "      <th>Total_Charges</th>\n",
       "      <th>Subscription_Type</th>\n",
       "      <th>Payment_Method</th>\n",
       "      <th>Login_Frequency</th>\n",
       "      <th>Support_Tickets</th>\n",
       "      <th>Complaints</th>\n",
       "      <th>Discount_Received</th>\n",
       "      <th>Contract_Type</th>\n",
       "      <th>Last_Login_Days</th>\n",
       "      <th>Usage_Hours</th>\n",
       "      <th>Customer_Satisfaction</th>\n",
       "      <th>Churn</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>CUST10001</td>\n",
       "      <td>22</td>\n",
       "      <td>Male</td>\n",
       "      <td>Pune</td>\n",
       "      <td>17</td>\n",
       "      <td>1902.78</td>\n",
       "      <td>32226.17</td>\n",
       "      <td>Basic</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>17</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>No</td>\n",
       "      <td>Quarterly</td>\n",
       "      <td>11</td>\n",
       "      <td>48.3</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>CUST10002</td>\n",
       "      <td>59</td>\n",
       "      <td>Male</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>26</td>\n",
       "      <td>2489.35</td>\n",
       "      <td>63164.14</td>\n",
       "      <td>Standard</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>Yearly</td>\n",
       "      <td>15</td>\n",
       "      <td>18.6</td>\n",
       "      <td>7.1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>CUST10003</td>\n",
       "      <td>52</td>\n",
       "      <td>Female</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>62</td>\n",
       "      <td>293.25</td>\n",
       "      <td>17398.45</td>\n",
       "      <td>Premium</td>\n",
       "      <td>UPI</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Monthly</td>\n",
       "      <td>2</td>\n",
       "      <td>64.0</td>\n",
       "      <td>4.9</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>CUST10004</td>\n",
       "      <td>41</td>\n",
       "      <td>Female</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>8</td>\n",
       "      <td>762.31</td>\n",
       "      <td>6087.82</td>\n",
       "      <td>Basic</td>\n",
       "      <td>UPI</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>No</td>\n",
       "      <td>Monthly</td>\n",
       "      <td>25</td>\n",
       "      <td>24.5</td>\n",
       "      <td>6.7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>CUST10005</td>\n",
       "      <td>40</td>\n",
       "      <td>Male</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>8</td>\n",
       "      <td>1573.80</td>\n",
       "      <td>13139.40</td>\n",
       "      <td>Basic</td>\n",
       "      <td>UPI</td>\n",
       "      <td>12</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Monthly</td>\n",
       "      <td>32</td>\n",
       "      <td>40.8</td>\n",
       "      <td>7.6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9995</th>\n",
       "      <td>CUST19996</td>\n",
       "      <td>42</td>\n",
       "      <td>Male</td>\n",
       "      <td>Pune</td>\n",
       "      <td>61</td>\n",
       "      <td>1892.20</td>\n",
       "      <td>120738.31</td>\n",
       "      <td>Premium</td>\n",
       "      <td>Net Banking</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>No</td>\n",
       "      <td>Quarterly</td>\n",
       "      <td>7</td>\n",
       "      <td>24.8</td>\n",
       "      <td>4.3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9996</th>\n",
       "      <td>CUST19997</td>\n",
       "      <td>70</td>\n",
       "      <td>Male</td>\n",
       "      <td>Ahmedabad</td>\n",
       "      <td>18</td>\n",
       "      <td>1459.04</td>\n",
       "      <td>25312.24</td>\n",
       "      <td>Premium</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>No</td>\n",
       "      <td>Quarterly</td>\n",
       "      <td>20</td>\n",
       "      <td>45.2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9997</th>\n",
       "      <td>CUST19998</td>\n",
       "      <td>36</td>\n",
       "      <td>Male</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>49</td>\n",
       "      <td>1580.60</td>\n",
       "      <td>82169.82</td>\n",
       "      <td>Standard</td>\n",
       "      <td>UPI</td>\n",
       "      <td>16</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>Quarterly</td>\n",
       "      <td>13</td>\n",
       "      <td>69.6</td>\n",
       "      <td>10.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9998</th>\n",
       "      <td>CUST19999</td>\n",
       "      <td>47</td>\n",
       "      <td>Male</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>3</td>\n",
       "      <td>2436.46</td>\n",
       "      <td>7256.01</td>\n",
       "      <td>Basic</td>\n",
       "      <td>Net Banking</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>Yearly</td>\n",
       "      <td>17</td>\n",
       "      <td>34.4</td>\n",
       "      <td>7.8</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9999</th>\n",
       "      <td>CUST20000</td>\n",
       "      <td>50</td>\n",
       "      <td>Male</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>11</td>\n",
       "      <td>550.67</td>\n",
       "      <td>5677.32</td>\n",
       "      <td>Standard</td>\n",
       "      <td>UPI</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>No</td>\n",
       "      <td>Quarterly</td>\n",
       "      <td>20</td>\n",
       "      <td>38.9</td>\n",
       "      <td>7.4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10000 rows × 18 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Customer_ID  Age  Gender   Location  Tenure_Months  Monthly_Charges  \\\n",
       "0      CUST10001   22    Male       Pune             17          1902.78   \n",
       "1      CUST10002   59    Male    Chennai             26          2489.35   \n",
       "2      CUST10003   52  Female     Mumbai             62           293.25   \n",
       "3      CUST10004   41  Female    Chennai              8           762.31   \n",
       "4      CUST10005   40    Male  Hyderabad              8          1573.80   \n",
       "...          ...  ...     ...        ...            ...              ...   \n",
       "9995   CUST19996   42    Male       Pune             61          1892.20   \n",
       "9996   CUST19997   70    Male  Ahmedabad             18          1459.04   \n",
       "9997   CUST19998   36    Male      Delhi             49          1580.60   \n",
       "9998   CUST19999   47    Male    Chennai              3          2436.46   \n",
       "9999   CUST20000   50    Male    Kolkata             11           550.67   \n",
       "\n",
       "      Total_Charges Subscription_Type Payment_Method  Login_Frequency  \\\n",
       "0          32226.17             Basic    Credit Card               17   \n",
       "1          63164.14          Standard    Credit Card               13   \n",
       "2          17398.45           Premium            UPI               20   \n",
       "3           6087.82             Basic            UPI                9   \n",
       "4          13139.40             Basic            UPI               12   \n",
       "...             ...               ...            ...              ...   \n",
       "9995      120738.31           Premium    Net Banking                9   \n",
       "9996       25312.24           Premium    Credit Card               11   \n",
       "9997       82169.82          Standard            UPI               16   \n",
       "9998        7256.01             Basic    Net Banking               10   \n",
       "9999        5677.32          Standard            UPI               11   \n",
       "\n",
       "      Support_Tickets  Complaints Discount_Received Contract_Type  \\\n",
       "0                   0           1                No     Quarterly   \n",
       "1                   1           0                No        Yearly   \n",
       "2                   1           1               Yes       Monthly   \n",
       "3                   3           1                No       Monthly   \n",
       "4                   2           0               Yes       Monthly   \n",
       "...               ...         ...               ...           ...   \n",
       "9995                2           1                No     Quarterly   \n",
       "9996                1           1                No     Quarterly   \n",
       "9997                2           0                No     Quarterly   \n",
       "9998                1           0                No        Yearly   \n",
       "9999                1           1                No     Quarterly   \n",
       "\n",
       "      Last_Login_Days  Usage_Hours  Customer_Satisfaction  Churn  \n",
       "0                  11         48.3                    5.0      1  \n",
       "1                  15         18.6                    7.1      0  \n",
       "2                   2         64.0                    4.9      0  \n",
       "3                  25         24.5                    6.7      1  \n",
       "4                  32         40.8                    7.6      1  \n",
       "...               ...          ...                    ...    ...  \n",
       "9995                7         24.8                    4.3      1  \n",
       "9996               20         45.2                    NaN      1  \n",
       "9997               13         69.6                   10.0      1  \n",
       "9998               17         34.4                    7.8      1  \n",
       "9999               20         38.9                    7.4      0  \n",
       "\n",
       "[10000 rows x 18 columns]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(r\"C:\\Users\\DELL\\OneDrive\\Desktop\\customer-churn-ml\\data\\raw\\customer_churn.csv\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c52ee551-0b00-4ab3-a0e9-bbcca8fc8703",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Customer_ID', 'Age', 'Gender', 'Location', 'Tenure_Months', 'Monthly_Charges', 'Total_Charges', 'Subscription_Type', 'Payment_Method', 'Login_Frequency', 'Support_Tickets', 'Complaints', 'Discount_Received', 'Contract_Type', 'Last_Login_Days', 'Usage_Hours', 'Customer_Satisfaction', 'Churn']\n"
     ]
    }
   ],
   "source": [
    "print(df.columns.tolist())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4d3b85be-6288-4503-b21c-e7dae1f17a0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Customer_ID                  str\n",
       "Age                        int64\n",
       "Gender                       str\n",
       "Location                     str\n",
       "Tenure_Months              int64\n",
       "Monthly_Charges          float64\n",
       "Total_Charges            float64\n",
       "Subscription_Type            str\n",
       "Payment_Method               str\n",
       "Login_Frequency            int64\n",
       "Support_Tickets            int64\n",
       "Complaints                 int64\n",
       "Discount_Received            str\n",
       "Contract_Type                str\n",
       "Last_Login_Days            int64\n",
       "Usage_Hours              float64\n",
       "Customer_Satisfaction    float64\n",
       "Churn                      int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "dc35eca3-8f8d-4e21-a903-eb1606852f44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Age                             int64\n",
      "Tenure_Months                   int64\n",
      "Monthly_Charges               float64\n",
      "Total_Charges                 float64\n",
      "Login_Frequency                 int64\n",
      "Support_Tickets                 int64\n",
      "Complaints                      int64\n",
      "Last_Login_Days                 int64\n",
      "Usage_Hours                   float64\n",
      "Customer_Satisfaction         float64\n",
      "Churn                           int64\n",
      "Gender_Male                      bool\n",
      "Location_Bangalore               bool\n",
      "Location_Chennai                 bool\n",
      "Location_Delhi                   bool\n",
      "Location_Hyderabad               bool\n",
      "Location_Kolkata                 bool\n",
      "Location_Mumbai                  bool\n",
      "Location_Pune                    bool\n",
      "Subscription_Type_Premium        bool\n",
      "Subscription_Type_Standard       bool\n",
      "Payment_Method_Credit Card       bool\n",
      "Payment_Method_Debit Card        bool\n",
      "Payment_Method_Net Banking       bool\n",
      "Payment_Method_UPI               bool\n",
      "Discount_Received_Yes            bool\n",
      "Contract_Type_Quarterly          bool\n",
      "Contract_Type_Yearly             bool\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "df_ml = df.drop([\"Customer_ID\"], axis=1)\n",
    "df_ml = pd.get_dummies(df_ml, drop_first=True)\n",
    "\n",
    "print(df_ml.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "9e062dfb-e240-468c-b41b-d6061350cee6",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df_ml.drop(\"Churn\", axis=1)\n",
    "y = df_ml[\"Churn\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "87bad6e6-a7c3-4d83-8b9c-942945f33ff1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Series([], dtype: object)\n"
     ]
    }
   ],
   "source": [
    "print(X.dtypes[X.dtypes == \"object\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "886756d1-ee7b-4c6a-8e11-ed504ff777c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Missing values in X:\n",
      "Monthly_Charges          100\n",
      "Usage_Hours              100\n",
      "Customer_Satisfaction    100\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"Missing values in X:\")\n",
    "print(X.isnull().sum()[X.isnull().sum() > 0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "52e8e76a-3ffe-48bd-b26d-7eda437f7525",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Missing values in y: 0\n"
     ]
    }
   ],
   "source": [
    "print(\"Missing values in y:\", y.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "6e070d19-1860-4d7c-be2e-e23bae81b59f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total missing values in X: 0\n"
     ]
    }
   ],
   "source": [
    "# Fill missing values in X with median\n",
    "X = X.fillna(X.median())\n",
    "\n",
    "# Check again\n",
    "print(\"Total missing values in X:\", X.isnull().sum().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "b4fb3dbc-9cdf-4dbc-9ec6-c8a2c06b5c08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training data: (8000, 27)\n",
      "Testing data: (2000, 27)\n"
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
    ")\n",
    "\n",
    "print(\"Training data:\", X_train.shape)\n",
    "print(\"Testing data:\", X_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "17f50cb0-a4ab-4f81-a2b5-562d284ff0cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logistic Regression trained successfully!\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\sklearn\\linear_model\\_logistic.py:599: ConvergenceWarning: lbfgs failed to converge after 3000 iteration(s) (status=1):\n",
      "STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT\n",
      "\n",
      "Increase the number of iterations to improve the convergence (max_iter=3000).\n",
      "You might also want to scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    }
   ],
   "source": [
    "logistic_model = LogisticRegression(\n",
    "    max_iter=3000,\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "logistic_model.fit(X_train, y_train)\n",
    "\n",
    "print(\"Logistic Regression trained successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "b190fe53-98a6-463a-911e-ece2c720b251",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X_train: (8000, 27)\n",
      "X_test: (2000, 27)\n",
      "y_train: (8000,)\n",
      "y_test: (2000,)\n"
     ]
    }
   ],
   "source": [
    "print(\"X_train:\", X_train.shape)\n",
    "print(\"X_test:\", X_test.shape)\n",
    "print(\"y_train:\", y_train.shape)\n",
    "print(\"y_test:\", y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "00e28226-4f99-44b3-beb4-60f27fc3f53c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logistic Regression trained successfully!\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\sklearn\\linear_model\\_logistic.py:599: ConvergenceWarning: lbfgs failed to converge after 1000 iteration(s) (status=1):\n",
      "STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT\n",
      "\n",
      "Increase the number of iterations to improve the convergence (max_iter=1000).\n",
      "You might also want to scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "logistic_model = LogisticRegression(\n",
    "    max_iter=1000,\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "logistic_model.fit(X_train, y_train)\n",
    "\n",
    "print(\"Logistic Regression trained successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "cb4d41aa-5593-4ca9-a332-bc0508d33761",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Decision Tree trained successfully!\n"
     ]
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "\n",
    "decision_tree_model = DecisionTreeClassifier(\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "decision_tree_model.fit(X_train, y_train)\n",
    "\n",
    "print(\"Decision Tree trained successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10674063-4222-485d-9df2-e45f1ea80b77",
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
   "version": "3.14.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
