using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameLevel1Script : MonoBehaviour
{
    
    public GameObject countdown_object = null;
    public float tmpTime = 0;

    void Start()
    {
        
    }

    void Update()
    {
        tmpTime += Time.deltaTime;
        if (tmpTime >= 1.0f)
        {
            tmpTime = 0;
            Text countdown_text = countdown_object.GetComponent<Text>();
            if (count > 0)
            {
                countdown_text.text = "" + count;
                count--;
            }
            else if (count == 0)
            {
                countdown_text.text = "START";
                count--;
            }
            else
            {
                count = 0;
                phase = 1;
                countdown_text.text = "";
            }
        }
    }
}
