package scrum;

public class ScrumMaster {

    private String nombre;
    private String rolSecundario;

    public ScrumMaster(String nombre) {
        this.nombre = nombre;
        this.rolSecundario = "";
    }
    
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String aNombre) {
        this.nombre = aNombre;
    }

    public String getRolSecundario() {
        return this.rolSecundario;
    }

    public void setRolSecundario(String aRolSecundario) {
        this.rolSecundario = aRolSecundario;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("ScrumMaster{");
        sb.append("nombre=").append(nombre);
        sb.append(", rolSecundario=").append(rolSecundario);
        sb.append('}');
        return sb.toString();
    }

}
