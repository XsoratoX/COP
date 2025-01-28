public class Heater extends AirConditioner{
    @Override
    public double function(double temperature){
        double result = temperature + 0.1;
        System.out.println("Now temperature: " + result);
        return result;
    }
}