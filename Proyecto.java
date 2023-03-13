import java.util.Vector;

public class Proyecto {
	private String nombre;
	private String fechaInicio;
	private Boolean estado;
	public Vector<Equipo> equipos = new Vector<Equipo>();
	public Vector<Stakeholder> stakeholders = new Vector<Stakeholder>();
	public Vector<Tareas> tareas = new Vector<Tareas>();

	public String getNombre() {
		return this.nombre;
	}

	public void setNombre(String aNombre) {
		this.nombre = aNombre;
	}

	public String getFechaInicio() {
		return this.fechaInicio;
	}

	public void setFechaInicio(String aFechaInicio) {
		this.fechaInicio = aFechaInicio;
	}

	public Boolean getEstado() {
		return this.estado;
	}

	public void setEstado(Boolean aEstado) {
		this.estado = aEstado;
	}
}