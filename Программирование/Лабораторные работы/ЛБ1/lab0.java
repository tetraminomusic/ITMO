
import java.util.Arrays;
import java.util.Random;
import static java.lang.Math.*;

public class lab0 {

    // 1 функция

    public static float frst_func(float x1) {
        return (float) pow((pow(exp(1) , 2*(3-x1))) , (0.5) / (1 - atan(1 / (pow(exp(1) , (float) abs(x1))))));
    }

    // 2 функция

    public static float scnd_func(float x1) {
        return (float) log((float) pow(exp(1) , asin(sin(x1))));
    }



    // 3 функция

    public static float thrd_func(float x1) {
        return (float) pow(((double) 2/3) * (1 - (float) asin(sin(x1))) , 2*(tan((float) log((float) cos(x1) * (float) cos(x1))) + 1));
    }

    // функция округления

    public static float ceiling (float x1) {
        return (float) round(x1 * 100.0) / 100;
    }

    // функция вывода массива в понятном виде


    public static void main(String[] args) {

        float max_length = 0;

        // создаём 1-ый массив

        int[] w1 = new int[(19-5)/2+1];
        int number = 0;
        for (int i = 19; i >= 5; i--) {
            if (i % 2 != 0) {
                w1[number] = i;
                number++;
            }
        }

        // создаём 2-ой массив

        float[] x = new float[18];
        Random random = new Random();
        for (int i = 0; i < 18; i++) {
            float num = random.nextFloat((7+12)+1)-12;
            x[i] = num;
        }

        // работаем с 2-мерным массивом

        float[][] w = new float[8][18];
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 18; j++) {
                if (w1[i] == 11) {
                    w[i][j] = ceiling(frst_func(x[j]));
                    max_length = max(max_length, abs(w[i][j]));
                } else if (w1[i] == 5 || w1[i] == 7 || w1[i] == 13 || w1[i] == 17) {
                    w[i][j] = ceiling(scnd_func(x[j]));
                    max_length = max(max_length, abs(w[i][j]));
                } else {
                    w[i][j] = ceiling(thrd_func(x[j]));
                    max_length = max(max_length, abs(w[i][j]));

                }
            }
        }
        int N = String.valueOf(max_length).length();
        for (float[] row : w) {
            for (float num : row) {
                System.out.printf("%" + (N+1) + "s ", num);
            }
            System.out.println();
        }
    }
}
