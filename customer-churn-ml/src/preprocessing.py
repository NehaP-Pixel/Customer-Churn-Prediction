{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e6967ea3-7626-4ef9-a0cf-fc4c1476f142",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3d3d898e-6d68-4969-9d01-579284d64832",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(r\"C:\\Users\\DELL\\OneDrive\\Desktop\\customer-churn-ml\\data\\raw\\customer_churn.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "83356a8f-b8e9-40cc-9931-4b4e916e4bfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10000"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Number of records \n",
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "680e59af-f152-48c1-907a-051322d364ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Number of features \n",
    "len(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "06c18eb4-515c-445b-a802-59bc9b300282",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Customer_ID', 'Age', 'Gender', 'Location', 'Tenure_Months',\n",
       "       'Monthly_Charges', 'Total_Charges', 'Subscription_Type',\n",
       "       'Payment_Method', 'Login_Frequency', 'Support_Tickets', 'Complaints',\n",
       "       'Discount_Received', 'Contract_Type', 'Last_Login_Days', 'Usage_Hours',\n",
       "       'Customer_Satisfaction', 'Churn'],\n",
       "      dtype='str')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Numberical Columns \n",
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d7985b09-5df5-4fcd-8f55-f1088bdac783",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_19300\\1107208828.py:2: Pandas4Warning: For backward compatibility, 'str' dtypes are included by select_dtypes when 'object' dtype is specified. This behavior is deprecated and will be removed in a future version. Explicitly pass 'str' to `include` to select them, or to `exclude` to remove them and silence this warning.\n",
      "See https://pandas.pydata.org/docs/user_guide/migration-3-strings.html#string-migration-select-dtypes for details on how to write code that works with pandas 2 and 3.\n",
      "  df.select_dtypes(include=\"object\").columns\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Index(['Customer_ID', 'Gender', 'Location', 'Subscription_Type',\n",
       "       'Payment_Method', 'Discount_Received', 'Contract_Type'],\n",
       "      dtype='str')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Categorical Columns \n",
    "df.select_dtypes(include=\"object\").columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "efa3c167-e823-4f6d-874f-8948c57fcd8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Churn\n",
       "1    5780\n",
       "0    4220\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Target variable\n",
    "df[\"Churn\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "43f1edf7-cbba-44a0-8eda-228f2af2b956",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Customer_ID                0\n",
       "Age                        0\n",
       "Gender                     0\n",
       "Location                   0\n",
       "Tenure_Months              0\n",
       "Monthly_Charges          100\n",
       "Total_Charges              0\n",
       "Subscription_Type          0\n",
       "Payment_Method             0\n",
       "Login_Frequency            0\n",
       "Support_Tickets            0\n",
       "Complaints                 0\n",
       "Discount_Received          0\n",
       "Contract_Type              0\n",
       "Last_Login_Days            0\n",
       "Usage_Hours              100\n",
       "Customer_Satisfaction    100\n",
       "Churn                      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Missing Values \n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a23b9520-97b2-432a-ae00-1300097e996f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Duplicate Records \n",
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ea574e21-b7b9-4387-80f7-939603a609a7",
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
       "      <th>Age</th>\n",
       "      <th>Tenure_Months</th>\n",
       "      <th>Monthly_Charges</th>\n",
       "      <th>Total_Charges</th>\n",
       "      <th>Login_Frequency</th>\n",
       "      <th>Support_Tickets</th>\n",
       "      <th>Complaints</th>\n",
       "      <th>Last_Login_Days</th>\n",
       "      <th>Usage_Hours</th>\n",
       "      <th>Customer_Satisfaction</th>\n",
       "      <th>Churn</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>9900.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>9900.000000</td>\n",
       "      <td>9900.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>43.804400</td>\n",
       "      <td>36.504900</td>\n",
       "      <td>1353.787783</td>\n",
       "      <td>49404.930584</td>\n",
       "      <td>12.014800</td>\n",
       "      <td>1.501900</td>\n",
       "      <td>0.709200</td>\n",
       "      <td>11.854400</td>\n",
       "      <td>35.192727</td>\n",
       "      <td>6.953727</td>\n",
       "      <td>0.578000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>15.224826</td>\n",
       "      <td>20.921939</td>\n",
       "      <td>663.708501</td>\n",
       "      <td>39825.688568</td>\n",
       "      <td>5.917473</td>\n",
       "      <td>1.223334</td>\n",
       "      <td>0.854347</td>\n",
       "      <td>11.986107</td>\n",
       "      <td>17.384849</td>\n",
       "      <td>1.747440</td>\n",
       "      <td>0.493903</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>199.110000</td>\n",
       "      <td>203.720000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>31.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>779.710000</td>\n",
       "      <td>16936.115000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>5.700000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>44.000000</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>1351.335000</td>\n",
       "      <td>38560.090000</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>34.900000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>57.000000</td>\n",
       "      <td>55.000000</td>\n",
       "      <td>1939.357500</td>\n",
       "      <td>73665.472500</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>17.000000</td>\n",
       "      <td>47.000000</td>\n",
       "      <td>8.200000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>70.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>2498.960000</td>\n",
       "      <td>190535.320000</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>149.000000</td>\n",
       "      <td>100.600000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Age  Tenure_Months  Monthly_Charges  Total_Charges  \\\n",
       "count  10000.000000   10000.000000      9900.000000   10000.000000   \n",
       "mean      43.804400      36.504900      1353.787783   49404.930584   \n",
       "std       15.224826      20.921939       663.708501   39825.688568   \n",
       "min       18.000000       1.000000       199.110000     203.720000   \n",
       "25%       31.000000      18.000000       779.710000   16936.115000   \n",
       "50%       44.000000      37.000000      1351.335000   38560.090000   \n",
       "75%       57.000000      55.000000      1939.357500   73665.472500   \n",
       "max       70.000000      72.000000      2498.960000  190535.320000   \n",
       "\n",
       "       Login_Frequency  Support_Tickets    Complaints  Last_Login_Days  \\\n",
       "count     10000.000000     10000.000000  10000.000000     10000.000000   \n",
       "mean         12.014800         1.501900      0.709200        11.854400   \n",
       "std           5.917473         1.223334      0.854347        11.986107   \n",
       "min           0.000000         0.000000      0.000000         0.000000   \n",
       "25%           8.000000         1.000000      0.000000         3.000000   \n",
       "50%          12.000000         1.000000      1.000000         8.000000   \n",
       "75%          16.000000         2.000000      1.000000        17.000000   \n",
       "max          37.000000         8.000000      6.000000       149.000000   \n",
       "\n",
       "       Usage_Hours  Customer_Satisfaction         Churn  \n",
       "count  9900.000000            9900.000000  10000.000000  \n",
       "mean     35.192727               6.953727      0.578000  \n",
       "std      17.384849               1.747440      0.493903  \n",
       "min       1.000000               1.000000      0.000000  \n",
       "25%      23.000000               5.700000      0.000000  \n",
       "50%      34.900000               7.000000      1.000000  \n",
       "75%      47.000000               8.200000      1.000000  \n",
       "max     100.600000              10.000000      1.000000  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Outliears \n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "af1cd080-a42d-4e70-8863-901e633a7466",
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
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Data type\n",
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "91c90d87-1b0d-414d-ab2b-8035be8d18a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age         0\n",
       "Gender      0\n",
       "Location    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Demographic information \n",
    "df[[\"Age\", \"Gender\", \"Location\"]].isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ad1ba611-cb82-465b-97b8-9ced8d899082",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Filling the missing values\n",
    "#Monthly_Charges\n",
    "df[\"Monthly_Charges\"] = df[\"Monthly_Charges\"].fillna(\n",
    "    df[\"Monthly_Charges\"].median()\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ed4fa6c3-03f4-431b-8125-449f5862329a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Usage Hours \n",
    "df[\"Usage_Hours\"] = df[\"Usage_Hours\"].fillna(\n",
    "    df[\"Usage_Hours\"].median()\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2cf597a0-3c08-4a56-b40e-3817a9b5483a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Customer Satisfaction\n",
    "df[\"Customer_Satisfaction\"] = df[\"Customer_Satisfaction\"].fillna(\n",
    "    df[\"Customer_Satisfaction\"].median()\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "4a6f327c-bd96-4ef2-8105-e80a5d32f3cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Customer_ID              0\n",
       "Age                      0\n",
       "Gender                   0\n",
       "Location                 0\n",
       "Tenure_Months            0\n",
       "Monthly_Charges          0\n",
       "Total_Charges            0\n",
       "Subscription_Type        0\n",
       "Payment_Method           0\n",
       "Login_Frequency          0\n",
       "Support_Tickets          0\n",
       "Complaints               0\n",
       "Discount_Received        0\n",
       "Contract_Type            0\n",
       "Last_Login_Days          0\n",
       "Usage_Hours              0\n",
       "Customer_Satisfaction    0\n",
       "Churn                    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d0fd28f5-7942-4b51-a037-4090dc2697e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1a0e8b50-641f-490d-958f-3407f016f2eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Invalid Values \n",
    "#Age \n",
    "(df[\"Age\"] < 0).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d33f7d3b-465d-44e9-9dc5-d2807e1bb219",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Monthly Charges \n",
    "(df[\"Monthly_Charges\"] < 0).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "459e8185-ab19-4059-a2fb-4fa64e030f13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Tenure\n",
    "(df[\"Tenure_Months\"] < 0).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6322a291-27df-4634-8d08-0b09e141c783",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Satisfaction \n",
    "(\n",
    "    (df[\"Customer_Satisfaction\"] < 1) |\n",
    "    (df[\"Customer_Satisfaction\"] > 10)\n",
    ").sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e47b0c4f-0032-4c27-bb81-baa69f9f5d9d",
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
