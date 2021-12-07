# WSA_APKInstallTool
 A simple tool for intalling apk to WSA (or other Android emulators)

## Settings
You can change the port by editing `config.json`


## Others
The program may not respond during installation.



<img width="50%" src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAvIAAAIwCAIAAABr2RikAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAgAElEQVR4nO3dX2xc130n8HNHpExb1j87lv8ssnYSUm4VF92gLRCRKPSwXaxIe1Uv0A3gpzxUIAHBhoUaeVggDy2QYh8CLaR1ICwJJUFeaiBYdB0mIvW2UANS2ThB+sdhGnMS213XtiT/kSzLoimRdx/mD4fDmeHMcMiZOfx8EDg2eefe371zOPc7555zb/Lee++FENI0Lf4zhLC8vJz7l6WlpVu3bl27du3TTz9dXFxcWlq6c+dO2ELFkiLT0H5t5UF45513fzB5vuyHu3ff++TIf9y3b189a3jttezFv5tZWrrzh3/wpT/4gy8lSdJQAR34jv/87Z//+uo/hxDu6un7D/3/Yc9deyou9vqHr//kX34SQvjyv/3y5/Z/bsvK+z+//T/v3Hg7hLC3b9+f9P/JXTvu2rJNQwih0b/xrtCSnXJkWqKnp2fHjh07d+6866679uzZs2vXrh07duR+lclkyqpKkqQnlGSa0nBz586dy5cvf/jhh0tLS7mlW3W+6cDz1lrViuyK4lsvXWketX366adzc/+8tHQnhPDLuX9+7LFH77//vs2vb3Pt68vnuSSETJKpttjDux/efdfujz69/voHv31036M1lmytPX17crEmCUkSIvwYpcN11Kdiq066LdmpzT4yje5sSw5Oozu18Y3euXNnaWlpcXHx448//uCDDzKZzL59+x566KGenp7l5eXSQJMrL7l69WrpGSv371euXLl69ery8nKaprt27XrwwQf379/f19fX19dXTEkAAJvqzp07CwsLCwsL165du3z58s2bN5MkyWQyDzzwwIEDB3JpJvfPXOdNcuXKldJMc+fOnTfffPPmzZshhAceeOALX/jC7t2727c7AAB5N27c+M1vfnP16tUQwq5dux599NGenp5QSDZJkiSXL18OhW6lhYWF119//fbt2319fb//+7+/Z0/lMQQAAO3y0Ucf/eM//uOtW7d6e3s///nP33XXXaGYbC5fvlwcTDM/P3/79u0DBw587nOfk2kAgM5048aNN95449133+3t7R0YGCj22WSKw4TffPPN27dv792794knnpBpAICOtXv37ieeeOK+++67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85VvsFexmubezUNfy71u5WUNbjafEapcVGm5Vhyr9m+3XXsBtFGSeyDUsWPHtnrDSZJ251BlNmh6LBmZyM1hjv7Usp32FaDE1p/lz58/nyRJ1/fW0IGmx2qMUijMw6pv4j0A1E+sofVqzb0vzpJu6R2QASCINWyGwpShMDEyVD5naMDUWgA2i1jDJuh/fiY/znd2YmQgyRsYGJmYDbl79LppPQCtJ9awOYqzsNZMQpmfqXCPXgDYuO5/gjcdq79/eHxme/fKDI+n6Xi7iwDYPvTWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIRMbzJgGACKRpqrcGAIiEWAMAREKsAQAiIdYAAJEQawCArpebAiXWAACREGsAgEiINQBAJMQaACASYg0AEIlMKAweBgDoanprAIBIiDUAQCTEGgAgEmINABAJsQYAiISZUABAJPTWAACREGsAgEiINQBAJMQaACASYg0AEImeNE3NhAIAulouzOitAQAiIdYAAJEQawCASIg1AEAkMsvLy+2uAQBgo9I01VsDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIiHWAACRyIQQ0jRtdxkAAM3LhRm9NQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIpFJ07TdNQAAbFSapnprAIBIiDUAQCTEGgAgEmINABAJsQYAiIRYAwBEQqwBACIh1gAAkRBrAIBIiDUAQCQyIQTPTwAAulouzOitAQAiIdYAAJEQawCASIg1AEAkxBoAIBIZ06AAgAikaaq3BgCIhFgDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIpEJIXgsFAAQAb01AEAkxBoAIBJiDQAQCbEGAIiEWAMAdL3c/CexBgCIhFgDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIRCZN03bXAACwUWma6q0BACIh1gAAkRBrAIBIiDUAQCTEGgAgEmINABCJTAjh7Q/M8QYAul7mX66mF19dancZAAAblfmH15eXlttdBQDAhmWuf+IKFAAQg0wIoW9nu6sAANiwTAjh3r6k3WUAAGxUJoRwz13trgIAYMPctwYAiEQmhHDr03ZXAQCwYZkQwo0Fk6EAgK7XE9KwoLcGAOhmaZqGEDK9Pe0uBACgFTKHPpsJ5ncDAN2v54v/NvPpHWNrAICul8lkwh/272h3GQAAG+W+NQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0A0PXSNA1iDQAQDbEGAIiEWAMAREKsAQAiIdYAAJHIhMLgYQCALmUmFAAQFbEGAIiEWAMAREKsAQAiIdYAAJHImAYFAEQgTVO9NQBAJMQaACASYg0AEAmxBgCIhIcnAACR0FsDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIiHWAACRyKRp6plQAEC3S9NUbw0AEAmxBgCIhFgDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIRMaTEwCAOOitAQAiIdYAAJEQawCASIg1AEAkxBoAIBJiDQAQCbEGAIiEWAMAREKsAQAiIdYAAJEQawCASIg1AEAkxBoAIBJiDQAQCbEGAIiEWAMAREKsAQAikQkhpGna7jIAAJqXCzN6awCASIg1AEAkxBoAIBJiDQAQiYzxwgBABNI01VsDAERCrAEAIiHWAACREGsAgEiINQBAJMQaACASYg0AEAmxBgCIhFgDAERCrAEAIiHWAACRyCRJ0u4aAABaQG8NABAJsQYAiIRYAwBEQqwBACIh1gAAkcikadruGgAAWkBvDQAQCbEGAIiEWAMAREKsAQAiIdYAAJEQawCASIg1AEAkxBoAIBJiDQAQCbEGAIiEWAMAREKsAQAiIdYAAJEQawCASIg1AEAkxBoAIBJiDQAQCbEGAIiEWAMAREKsAQAiIdYAAJEQawCASIg1AEAkxBoAIBJiDQAQCbEGAIiEWAMARCITQkjTtN1lAAA0Lxdm9NYAAJHIhBCWbi21uwwAgI3KLC8uv/Pjd9pdBgDARmU+/OWHH795o91lAABsVOb6/LV21wAA0AKZxeuL7a4BAKAFMiENO3buaHcZAAAblQkhLC2aCQUAdD33rQEAIpEJIezo62l3GQAAG5UJISwt3Gl3GQAAG5XJ7HQdCgCIQebez97b7hoAAFogc9+/u7/nHmNrAICul+m7v++RP/k37S4DAGCjMiGEex68p91lAABslPHCAEAkxBoAIBJiDQAQCbEGAIiEWAMAREKsAQAiIdYAAJEQawCASIg1AEAkxBoAIBJiDcLNGJUAAA/BSURBVAAQCbEGAIiEWAMAREKsAQAi0XP79u00TdtdBgDARumtAQAiIdYAAJEQawCASIg1AEAkxBoAIBJiDQAQCbEGAIiEWAMAREKsAQAikQkhuMswABABvTUAQCTEGgAgEmINABAJsQYAiIRYAwB0vdz8J7EGAIiEWAMAREKsAQAiIdYAAJEQawCASGQ8OQEAiENPG7edJEkbtw4ARKZtsUYvEQDQWsbWAACREGsAgEiINQBAJDLB0F0AoMslSZKmqd4aACASYg0AEAmxBgCIhFgDAERCrAEAIpHJjRxudxkAABultwYAiIRYAwBEQqwBACIh1gAAkRBrAICul6ZpkiRiDQAQCbEGAIiEWAMAREKsAQAiIdYAAJHIeHICABAHvTUAQCTEGgAgEmINABCJnt7e3u0wvOb69evtLoEN2bt3b7tL2FyaaLfTROlw0TfRnJ52F7Clbt++/e677y4sLCwvL7e7Fta3e/fuBx54oLe3t92FbB1NtLtoonS4bdhEt1GsuX379htvvHHgwIH+/v4dO3a0uxzWsbS09P7777/55puPPvroNvmb1ES7iyba7nJYxzZsommabqOxNVevXn344Ycffvhhf41dYceOHQcOHDhw4MDly5fbXcsW0US7iyZKh9uGTTRsqyHDN27cuP/++9tdBY05cODAwsJCu6vYIppoN9JE6XDbqomGbRVrQgi+YXSdTCaztLTU7iq2jibadTRROtx2a6LbK9YAABETawCASIg1AEDXS5IkiDUAQDTEGgAgEmINABAJsQYAiIRYAwBEIpMbOQwA0L3SNA16a1ohe+HFE0eOHNlZdOTIkRMvXsi2u662yV448eKFdhfBRmU1bDrGhRO5Jvji1jW/jX2OZV/M/eWcuFD9J2wOsWYjshdOHNm589CxF85dunRp5ceXLl0698KxQzuPnNjCv8HOkL1w4sjOQ8fO/ard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Ly7OTZ46XjppMITDhw8fPzU5t3jxbMVP5v6jZ3PnjcMlrzg+OVf6OIUtUKGMcLhYSPnCz11cPTfy8OHjk3OLa089/c99uzAEj67Vf7TQsg+XN49Tk3OLi2UPby3zZ9++WNpW8m1q7d9CQy0QNqxigzt+qkKDq/w5tmaGeO7VF88+dzR/jUt3TSdI/uZv/iaE8Mwzz7S7ks11/fr1X//611/60pfaXQgN+8UvfvH444/v3bu33YVsru5vohdO7Mw95LJ6T06kNFE63DZpot///veTJNFbAwBEIpMkicdCAQBdLTetW28NABAJsQYAiERPuwsA4nD07OLi2XYXAWxzemsAgEiINQBA10vT1ARvACAeYg0AEIltFGsymczS0lK7q6Axy8vL7S5h62ii3UgTpcNtqyYatlWs6evru3LlSruroDHvvffenj172l3FFtFEu5EmSofbVk00bKtY89BDD125cuXq1au+bXSFpaWld95555133vnMZz7T7lq2iCbaXTRROtw2bKJhW923pre397HHHvvtb3/793//954X0fl6enr27dv3hS98obe3t921bBFNtLtoou0uh3VswyYatlWsCSH09vY+/vjjjz/+eLsLgco0UTqcJkqH2y6xJvoHstPtNFE6nCZKV9hGY2sAgLiJNQBAJMQaACASmdwzFNpdBgBA83JhRm8NABAJsQYAiIRYAwBEQqwBACIh1gAAkciYBgUAxEFvDQAQCbEGAIiEWAMAREKsAQAiIdYAAJEQawCASGRCCHdu3Wl3GQAAG5VZWlx69+/eaXcZAAAblbn2yw8//peP210GAMBGZa7PX293DQAALZBZvL6YhrTdZQAANC9N0xBCJk3TzE7zoQCArpcJISwvLre7DACAjcqEEJLgId4AQBdLkiTkYs2Ovh3tLgYAYKMySZosLSx98vEn7a4EAKAZt27dCiFkMplMZkcmhHDj/RvtLgkAoBkLCwtJkmQymczez+4NIdx83x35AICu9Omnn4YQent7M48MPdK7q/f1X7zR7pIAAJrx3nvvhRB6e3t7Hug/cOPff/xW9q12lwQA0IxcrNm1a1emr69v18O7er/Y+/7l99pdFQBAY65du/bee+9lMpl77rknkyTJvffem+nJZN/4TbsLAwBozPz8fAhh9+7dSZJkkiTZu3dvkiS//e1vP/jgg3bXBgBQrw8//PCNN97IZDL79u0Ludvx9fT07N27N4Twi1/84sMPP2xzgQAAdbh+/fo//dM/hRD27dvX09OTJEkmhJDrsLnrrrvefffdn//857lnYAIAdKw0Tf/hH/7h8uXLfX19+/btyz88If9/mcxnPvOZ3t7ey5cvX7p0SZ8NANCxrl+//rOf/ezdd9/t6el58MEHM5l8N03+/0IIvb29Dz74YG9v7+uvv/7jH//4/fffb3PJAABrfPDBBzMzM6+//npvb+/DDz/c29sbCmEm+elPf5q76rS0tJSm6Z07d65evbqwsJCm6Wc/+9nf+73fu++++9pcPgBACNeuXXv11Vf/9V//NUmSu+++O9cdE0JIil555ZXl5eVQiDUhhOXl5Y8++ujatWvLy8vLy8t79ux59NFHH3zwwV27du3ataunp6fN+wQAbA+Li4u3bt365JNPrl69+tZbb3300Ue5Zz/t379/3759mczKWJrcP5NXXnklTdM0TXMhJoSQCze3b9++fv36xx9/fOfOneIPc9KCij8v/ufy8nLxP8sWTtM0d5Hr85//fOnL69/PVo1r3uzx0blD2iE66qB1VDGwDeVOBh2+/lYVudk729BGu+LIN7qeRjda58Ep/mf+AlOS7Nix4957792/f395J01BT5IkaZoWX1A8SfT09Nx333179+799NNPb968ubi4uLS0dPv27Ybq3vhObvZJq9F3otF6Glp/t5yhN/VvclOP8GbrlneQdumo5toq7Tp5t8Wmnuk3ez0tWf9Wvq3FZNLT09PT07Nz585du3bdfffdO3bsqLhY7p//H5BR9lqkDROVAAAAAElFTkSuQmCC'>

